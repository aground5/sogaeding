#!/usr/bin/env python3
 #coding: utf-8
 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from konlpy.tag import Mecab
import json

from crawling_parsing import get_index_terms
import sys
from naver_news import today


def extract_keyword(nouns, doc):
	n_gram_range = (2, 3)

	count = CountVectorizer(ngram_range=n_gram_range).fit([nouns])
	candidates = count.get_feature_names_out()
 
	model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')
	doc_embedding = model.encode([doc])
	candidate_embeddings = model.encode(candidates)

	top_n = 8
	distances = cosine_similarity(doc_embedding, candidate_embeddings)
	keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
	return keywords


def word_count(nouns):
		""" 단어 빈도 dictionary를 생성한다. (key: word, value: frequency)
		
		return value: a sorted list of tuple (word, frequency) 
		"""
		freq = dict()
		for word in nouns:
			word = word.rstrip()
			freq[word] = freq.get(word, 0) + 1
		freq_items = list(freq.items())
		freq_items.sort(key=lambda x: -x[1])
		return freq_items

def get_key_words(f):
	mecab = Mecab()
	key_word = {}
	i = 0
	with open(f"data/{today}/news.txt", "r") as file:
		file_len = (len(file.readlines()) - 1) // 3
		file.seek(0)
		for line in file.readlines():
			line = line.strip()
			if not line:
				continue
			elif line[:5] == "url: ":
				url = line[5:]
				continue

			tagged = mecab.pos(line, flatten=False, join=False)
			nouns = get_index_terms(tagged)
			kwlst = extract_keyword(' '.join(nouns), line)
			key_word[url] = kwlst
			f.write('url: ' + url + '\n')
			f.write(', '.join(kwlst) + '\n\n')
			i += 1
			print(f"fin {i}/{file_len}", file = sys.stderr)
	return key_word

if __name__ == "__main__":
	try:
		key_word_file = open(f"data/{today}/key_word.txt", "wt")
		key_word_json = open(f"data/{today}/key_word.json", "w")
	except FileNotFoundError:
		print("file is not found")
		raise FileNotFoundError
	try:
		key_word = get_key_words(key_word_file)
		json.dump(key_word, key_word_json)
	finally:
		key_word_file.close()
		key_word_json.close()
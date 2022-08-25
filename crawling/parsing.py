def get_morph_tags(tagged):
	word_tuple_list = []
	for word in tagged:
		word_tuple = word.strip().split('/')
		if len(word_tuple) == 2:
			word_tuple_list.append(word_tuple)
		else:
			word_tuple_list.append(('/','SS'))
	return word_tuple_list

def is_term(word):
	return word == 'NNG' or word == 'NNP' or word == 'SL' or word == 'SH'

def get_index_terms(mt_list):
	""" 형태소 분석 결과(형태소-품사 쌍)로부터 색인어를 추출
	색인어는 품사가 일반명사(NNG), 고유명사(NNP), 영어(SL), 숫자(SN), 한자(SH)이어야 함
	동일 어절 내에서 인접하여 결합된 경우도 색인어로 추출(복합어)
	mt_list: a list of tuples (morpheme, tag)
	return value: a list of string (색인어 리스트)
	"""
	nouns = []
	for word_lst in mt_list:
		word_num = len(word_lst)

		i = 0
		while i < word_num:
			if is_term(word_lst[i][1]):
				nouns.append(word_lst[i][0])
				j = i + 1
				if  i + 1 == word_num:
					break
				while is_term(word_lst[j][1]):
					nouns.append(word_lst[j][0])
					j += 1
					if  j == word_num:
						break
				if j != i + 1:
					mixed = ''
					for x in range(i, j):
						mixed += word_lst[x][0]
					nouns.append(mixed)
				i = j
			i += 1    
	return nouns

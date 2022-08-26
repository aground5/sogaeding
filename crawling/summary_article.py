import datetime
from transformers import PreTrainedTokenizerFast
from tokenizers import SentencePieceBPETokenizer
from transformers import BartForConditionalGeneration
import torch
import os
import sys
import requests
from pprint import pprint
from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
from googletrans import Translator
####pip install transformers
####pip install googletrans==4.0.0-rc1



today = datetime.datetime.now().strftime("%Y%m%d")

from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration
from transformers import BartModel
from kobart import get_pytorch_kobart_model, get_kobart_tokenizer
kobart_tokenizer = get_kobart_tokenizer()
model = BartModel.from_pretrained(get_pytorch_kobart_model())

def summerize(text, model, tokenizer):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    print(text)
   # Generate Summary Text Ids
    summary_text_ids = model.generate(
        input_ids=input_ids,
        bos_token_id=model.config.bos_token_id,
        eos_token_id=model.config.eos_token_id,
        length_penalty=0.7, #길이에 대한 패널티, 1보다 작은 경우 더 짧은 문장,
                        #1보다 클 경우 길이가 더 긴 문장 유도
        max_length=100, #요약문 최대 길이 설정
        min_length=30,  #요약문 최소 길이 설정
        num_beams=4,    #문장 생성 시, 다음단어 탐색 영역 개수
    )
    summ = tokenizer.decode(summary_text_ids[0], skip_special_tokens=True)
    return summ
#model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
translator = Translator()


from googletrans import Translator

from transformers import PreTrainedTokenizerFast
from tokenizers import SentencePieceBPETokenizer
from transformers import BartForConditionalGeneration

model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
translator = Translator()


sum_eng_file = open(f"./data/{today}/summary_eng.txt", "wt")
with open(f"./data/{today}/selected_eng.txt", "rt") as engfile:
    for line in engfile.readlines():
        line = line.strip()
        
        if line[:5] == 'url: ':
            url = line[5:]
            continue
        elif not line:
          continue
        elif len(line)>3000:
          line = line[:3000]
          continue
        ARTICLE_TO_SUMMARIZE = line 
        #ARTICLE ~ == 원하는 영어 문장이 들어가야 함.
        inputs = tokenizer([ARTICLE_TO_SUMMARIZE], return_tensors='pt')
        summary_ids = model.generate(inputs['input_ids'], max_length=300, early_stopping=False)
        summary_ids
        result_sum = str([tokenizer.decode(g, skip_special_tokens=True) for g in summary_ids])
        result = translator.translate(result_sum, dest='ko')

        sum_eng_file.write('url: ' + url + '\n')
        sum_eng_file.write((result.text) + '\n\n')  
sum_eng_file.close()

#  Load Model and Tokenize

sum_kor_file = open(f"./data/{today}/summary_kor.txt", "wt")
with open(f"./data/{today}/selected_kor.txt", "rt") as korfile:
    model = BartForConditionalGeneration.from_pretrained("ainize/bart-news")
    tokenizer = PreTrainedTokenizerFast.from_pretrained("ainize/bart-news")
    for line in korfile.readlines():
        line = line.strip()
        if line[:5] == 'url: ':
            url = line[5:]
            continue
        elif not line:
            continue
        summarized = summerize(line, model, tokenizer)
        
        sum_kor_file.write('url: ' + url + '\n')
        sum_kor_file.write(summarized + '\n\n')  
sum_kor_file.close()

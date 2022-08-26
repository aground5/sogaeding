import pymysql
import datetime
import pickle
from bs4 import BeautifulSoup
from naver_news import today
import requests
import re

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

def get_title(url):
	response = requests.get(url, headers=headers)
	if response.status_code != 200:
		raise Exception()
	news_page = BeautifulSoup(response.text, 'html.parser')
	title = news_page.find('h2', {'class' : 'media_end_head_headline'})
	title = title.get_text()
	return re.sub("\[.*?\]|〈.*?〉|.앵커.|【.*】|※.*|공동취재사진", '', title)

date = datetime.datetime.now()
db_connect = pymysql.connect(host='localhost', port=3306,user='', passwd='', charset='utf8')
db_connected = db_connect.cursor()
diary_cmd = 'INSERT INTO earth_diary_diary ({},{},{},{})'	#date, country, content, keyword
news_cmd = 'INSERT INTO earth_diary_news ({},{},{})' #title, url, diary_id
selete_cmd = 'SELETE id FROM {} WHERE content={}' #table, content

sumfile = open(f"./data/{today}/summary_kor.txt", "rt")
with open(f"./data/{today}/key_word.pickle", "rb") as kwp:
	keyword_dict = pickle.load(kwp)

cntnt_key = []
ttl_url_id = []
for line in sumfile.readlines():
	line = line.strip()
	if not line:
		continue
	if line[:5] == 'url: ':
		url = line[5:]
		continue
	cntnt_key.append((line, keyword_dict[url]))
	dic_id = db_connected.execute(selete_cmd.format('earth_diary_diary', line))
	ttl_url_id.append((get_title(url), url, dic_id))




for content, keyword in cntnt_key:
	db_connected.execute(diary_cmd.format(date, '한국', content, keyword))
for title, url, did in ttl_url_id:
	db_connected.execute(news_cmd.format(title, url, did))
sumfile.close()

sumfile = open(f"./data/{today}/summary_eng.txt", "rt")
keywordsfile = open(f"./data/{today}/keyword_eng.txt", "rt")
for line in sumfile.readlines():
	line = line.strip()
	if not line:
		continue
	if line[:5] == 'url: ':
		url = line[5:]
  
	keyti = keywordsfile.readline().strip().split('///')
	keywords, title = keyti[0], keyti[1]
 
	db_connected.execute(diary_cmd.format(date, '미국', line, keywords))
	did = db_connected.execute(selete_cmd.format('earth_diary_news', line))
	db_connected.execute(news_cmd.format(title, url, did))
 
sumfile.close()
keywordsfile.close()
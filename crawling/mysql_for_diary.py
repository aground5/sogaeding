import pymysql
import datetime
import pickle
from bs4 import BeautifulSoup
from naver_news import today
import requests
import re
from img_scrapper.crawl import img_url
import json

secrets = json.loads(open('secrets.json').read())
sql = secrets["DATABASES"]["default"]
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
db_connect = pymysql.connect(host=sql["HOST"], port=sql["PORT"], user=sql["USER"], passwd=sql["PASSWORD"], charset='utf8')
db_connected = db_connect.cursor()
diary_cmd = 'INSERT INTO earth_diary_diary ({},{},{},{})'	#date, country, content, keyword
news_cmd = 'INSERT INTO earth_diary_news ({},{},{})' #title, url, diary_id
img_cmd = 'INSERT INTO earth_diary_news ({},{})'	#img_url, dia_id

selete_cmd = 'SELETE id FROM {} WHERE content={}' #table, content


with open(f"./data/{today}/key_word.pickle", "rb") as kwp:
	keyword_dict = pickle.load(kwp)

with open(f"./data/{today}/summary_kor.txt", "rt") as sumfile:
	cntnt_key = []
	ttl_url_id_img = []
	for line in sumfile.readlines():
		line = line.strip()
		if not line:
			continue
		if line[:5] == 'url: ':
			url = line[5:]
			continue
		cntnt_key.append((line, keyword_dict[url]))
		dic_id = db_connected.execute(selete_cmd.format('earth_diary_diary', line))
		
		img = img_url(keyword_dict[url][0], is_kor=True)[0]
		ttl_url_id_img.append((get_title(url), url, dic_id, img))

	for content, keyword in cntnt_key:
		db_connected.execute(diary_cmd.format(date, '한국', content, keyword))
	for title, url, did, img in ttl_url_id_img:
		db_connected.execute(news_cmd.format(title, url, did))
		db_connected.execute(img_cmd.format(img, did))


with open(f"./data/{today}/summary_eng.txt", "rt") as sumfile:
	with open(f"./data/{today}/keyword_eng.txt", "rt") as keywordsfile:
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
			img = img_url(keywords.replace(',', ''))[0]
			db_connected.execute(img_cmd.format(img, did))
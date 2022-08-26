import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from urllib import parse
from newspaper import Article
from naver_news import today


def get_content(url):
	arcti = Article(url)
	try:
		arcti.download()
		arcti.parse()
		arcti.nlp()
	except:
		return None
	return arcti.text, arcti.keywords, arcti.title
	

try:
    response = requests.get('https://trends.google.co.kr/trends/trendingsearches/daily/rss?geo=US', timeout=1)
except:
    raise

if response.status_code != 200:
	raise
ggt = ET.fromstring(response.text)
ET.register_namespace("atom", "http://www.w3.org/2005/Atom")
ET.register_namespace("ht","https://trends.google.co.kr/trends/trendingsearches/daily")
namespaces = {"ht":"https://trends.google.co.kr/trends/trendingsearches/daily"}
ggt = ggt.find("channel")

i = 0
news_pages = []
for issue in ggt.findall("item"):
	if i > 2:
		break
	title = issue.findtext("title")
	news = issue.find("ht:news_item", namespaces)
	url = news.find("ht:news_item_url", namespaces).text
	print(url)
	content, keywords, title = get_content(url)
	print(url)

	if not content:
		continue
	content = content.replace('\n', '')
	news_pages.append((url, content, keywords, title))
	i += 1

key_eng = open(f'./data/{today}/keyword_eng.txt', "wt")
with open(f'./data/{today}/selected_eng.txt', "wt") as sfile:
	for url, page, keywords, title in news_pages:
		sfile.write('url: ' + url + '\n')
		sfile.write(page + '\n\n')
		key_eng.write(', '.join(keywords[:3]) + '///' + title + '\n')
key_eng.close()
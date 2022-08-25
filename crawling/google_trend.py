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
	except:
		return None
	return arcti.text
	

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
	content = get_content(url)
	print(url)

	if not content:
		continue
	content = content.replace('\n', '')
	news_pages.append((url, content))
	i += 1
 
with open(f'./{today}/selected_eng.txt', "w") as sfile:
	for url, page in news_pages:
		sfile.write('url: ' + url + '\n')
		sfile.write(page + '\n\n')
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

class issue:
	def __init__(self, title, url):
		self.title = title
		self.url = url
		self.content = None
  
def get_content_nwt(title):
    
    

	
response = requests.get('https://trends.google.co.kr/trends/trendingsearches/daily/rss?geo=US')
ggt = ET.fromstring(response.text)
ET.register_namespace("atom", "http://www.w3.org/2005/Atom")
ET.register_namespace("ht","https://trends.google.co.kr/trends/trendingsearches/daily")
namespaces = {"ht":"https://trends.google.co.kr/trends/trendingsearches/daily"}
ggt = ggt.find("channel")

i = 0
for issue in ggt.findall("item"):
	if i > 3:
		break
	title = issue.findtext("title")
	news = issue.find("ht:news_item", namespaces)
	url = news.find("ht:news_item_url", namespaces).text
	content = get_content_nwt(title)
	if not content:
		content = get_content_espn(title)
	if not content:
		continue
	
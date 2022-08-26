import requests
import re
from bs4 import BeautifulSoup
import pickle
import datetime

today = datetime.datetime.now().strftime("%Y%m%d")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

def get_rankpages():
    response = requests.get('https://news.naver.com/main/ranking/popularDay.naver', headers=headers, timeout=3)
    if response.status_code != 200:
        raise Exception()
    ranking_main = BeautifulSoup(response.text, 'html.parser')
    tmp = ranking_main.findAll("a", {"class":"list_title nclicks('RBP.rnknws')"})
    top_news = {}
    for page in tmp:
        top_news[page.get_text().strip()] = page["href"]
    return top_news

def get_topnewspages(ranking_pages):
    top_news = []
    for page in ranking_pages.values():
        response = requests.get(page, headers=headers)
        if response.status_code != 200:
            raise Exception()
        tops = BeautifulSoup(response.text, 'html.parser')
        top_thumbs = tops.find_all('a', {'class' : "_es_pc_link"})
        for i, thumb in enumerate(top_thumbs):
            top_news.append(thumb["href"])
            if i > 5:
                break
    return top_news

def get_content(page):
    response = requests.get(page, headers=headers)
    if response.status_code != 200:
        raise Exception()
    text = BeautifulSoup(response.text, 'html.parser')
    content = text.find('div', {'class' : "go_trans _article_content", 'id' : 'dic_area'})
    content = re.sub("\[.*?\]|〈.*?〉|.앵커.|【.*】|※.*|공동취재사진", '', str(content.get_text()).replace("\n", "").strip(), flags=re.MULTILINE)
    return content

if __name__ == "__main__":
    top_news = get_rankpages()
    news_dict = {}
    try:
        new_pic = open(f"data/{today}/news.pickle", "wb")
    except FileNotFoundError:
        print("file is not found")
    with open(f'data/{today}/news.txt', "w") as file:
        for page in top_news.values():
            content = get_content(page)
            file.write('url: '+ str(page) + '\n')
            file.write(content + '\n\n')
            news_dict[page] = content
    try:
        pickle.dump(news_dict, new_pic)
    finally:
        new_pic.close()
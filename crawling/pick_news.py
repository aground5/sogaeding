import json
import datetime

from naver_news import today

def calc_freq(keyword_dict, f):
    freq = {}
    for keywords in keyword_dict.values():
        for word in keywords:
            freq[word] = freq.get(word, 0) + 1

    freq_items = list(freq.items())
    freq_items.sort(key=lambda x: -x[1])
    for word, fr in freq_items:
        f.write(word + ' ' + str(fr) + '\n')
    return freq_items

def get_news_keyword(keyword_dict, freq_items):
    url_set = set()
    cnt = 0
    for word, fr in freq_items:
        for url, key_words in keyword_dict.items():
            if word in key_words and url not in url_set:
                print(f"found {word}!!")
                print(url)
                url_set |= {url}
                cnt += 1
                break
        if cnt > 3:
            break
    return list(url_set)
        

if __name__ == "__main__":
    try:
        news_file = open(f"data/{today}/news.txt", "r")
        freq_file = open(f"data/{today}/freq.txt", "w")
    except FileNotFoundError:
        print("file is not found")

    with open(f"data/{today}/key_word.json", "rb") as f:
        keyword_dict = json.load(f)
    freq_items = calc_freq(keyword_dict, freq_file)
    news_file.close()
    freq_file.close()
    selected_url = get_news_keyword(keyword_dict, freq_items)
    with open(f"data/{today}/news.json", "rb") as f:
        news = json.load(f)
    with open(f"data/{today}/selected_kor.txt", "wt") as sel:
        for i in range(3):
            sel.write('url: ' + selected_url[i] + '\n')
            sel.write(news[selected_url[i]] + '\n\n')
            
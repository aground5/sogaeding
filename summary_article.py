import datetime

today = datetime.datetime.now().strftime("%Y%m%d")

sum_eng_file = open(f"./data/{today}/summary_eng.txt")
with open(f"./data/{today}/selected_eng", "rt") as engfile:
    for line in engfile.readlines():
        line = line.strip()
        if line[:5] == 'url: ':
            url = line[5:]
            continue
        elif not line:
            continue
        """여기에 요약하는 함수
        summarized = 함수
        """
        sum_eng_file.write('url: ' + url + '\n')
        sum_eng_file.write(summarized + '\n\n')  
sum_eng_file.close()
        
 
sum_kor_file = open(f"./data/{today}/summary_kor.txt")
with open(f"./data/{today}/selected_kor", "rt") as korfile:
    for line in korfile.readlines():
        line = line.strip()
        if line[:5] == 'url: ':
            url = line[5:]
            continue
        elif not line:
            continue
        """여기에 요약하는 함수
        summarized = 함수
        """
        sum_kor_file.write('url: ' + url + '\n')
        sum_kor_file.write(summarized + '\n\n')  
sum_kor_file.close()
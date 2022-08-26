#!/bin/bash
cd crawling
if [ `ls -l | grep "data" | wc -l` == 0 ]
then
mkdir /data
fi
TODAY=`date "+%Y%m%d"`
if [ `ls -l ./data| grep $TODAY | wc -l` == 0 ]
then 
mkdir /data/$TODAY
fi
<<<<<<< HEAD
echo "./naver_news.py start"
python3 ./naver_news.py
echo "./crawling_keyword.py start"
python3 ./crawling_keyword.py
echo "./pick_news.py start"
python3 ./pick_news.py
=======
echo "/naver_news.py start"
python3 /naver_news.py
echo "/crawling_keyword.py start"
python3 /crawling_keyword.py
echo "/pick_news.py start"
python3 /pick_news.py
echo "/summary_article.py start"
python3 /summary_article.py
>>>>>>> f40af947d95721e125c2e23d7a876708fc733400

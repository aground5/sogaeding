#!/bin/bash
mkdir /data
TODAY=`date "+%Y%m%d"`
if [ `ls -l | grep $TODAY | wc -l` == 0 ]
then 
mkdir /data/$TODAY
fi
echo "./naver_news.py start"
python3 ./naver_news.py
echo "./crawling_keyword.py start"
python3 ./crawling_keyword.py
echo "./pick_news.py start"
python3 ./pick_news.py
#!/bin/bash
cd crawling
if [ `ls -l | grep "data" | wc -l` == 0 ]
then
mkdir /data
fi
TODAY=`date "+%Y%m%d"`
if [ `ls -l | grep $TODAY | wc -l` == 0 ]
then 
mkdir $TODAY
fi
echo "./google_trend.py"
python3 google_trend.py
#!/bin/bash
cd /
if [ `ls -l | grep "data" | wc -l` == 0 ]
then
mkdir /data
fi
TODAY=`date "+%Y%m%d"`
if [ `ls -l ./data | grep $TODAY | wc -l` == 0 ]
then 
mkdir /data/$TODAY
fi
echo "./google_trend.py"
python3 ./google_trend.py
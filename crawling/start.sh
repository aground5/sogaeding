#!/bin/bash
cd /
bash korea.sh
bash america.sh
python3 ./summary_article.py
python3 ./mysql_for_diary.py
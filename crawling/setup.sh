#!/bin/sh
cd /
wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
tar xvfz mecab-0.996-ko-0.9.2.tar.gz
cd mecab-0.996-ko-0.9.2
#./configure --build=aarch64-unknown-linux-gnu
./configure --build=x86_64-unknown-linux-gnu
make -j check
make -j install

cd /
wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
tar xvfz mecab-ko-dic-2.1.1-20180720.tar.gz
cd mecab-ko-dic-2.1.1-20180720
./autogen.sh
#./configure --build=aarch64-unknown-linux-gnu
./configure --build=x86_64-unknown-linux-gnu
make -j
make -j install

cd /
git clone https://bitbucket.org/eunjeon/mecab-python-0.996.git
cd mecab-python-0.996
python setup.py build
cd /
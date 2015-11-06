#!/bin/bash

cd dump
wget -r -l 115 http://markos.gaivo.net
rm -rf posts
mkdir posts
for i in markos.gaivo.net/blog/index.html?p=*; { cp $i "posts/"`echo $i|awk -F"p=" '{print $2}'`".html"; }

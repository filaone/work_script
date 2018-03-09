#!/usr/bin/python
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import json
import io

filename = "/Users/cnetwork/Desktop/mylist.txt"
filehandle = open(filename, 'r')
newfile = "/Users/cnetwork/Desktop/pocketList.txt"
newhandle = open(newfile, 'w')
page = io.open(filename, encoding='utf-8')
soup = BeautifulSoup(page, 'html.parser')
cnt = 0;

for link in soup.find_all('li'):
    for content in link.find_all('a', class_='title'):
        name = content.get_text()
        cnt+=1
        print(name)
        newhandle.write(name.encode('utf-8').decode('ascii', 'ignore')+'\n')


print("count : ",cnt)
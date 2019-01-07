#!/usr/bin/python
#-*- coding:utf-8 -*-

import requests
import sys
import json

# 可配置
index_list = ['index_name_1', 'index_name_2', 'index_name_3']

# 勿动
if len(sys.argv) == 0:
    print("Usage : python checkdoc.py $doc_id")
    sys.exit(0)


doc_id = sys.argv[1]
elastic_link_template = 'http://11.111.11.11:9200/{}/document/_search'
query = json.dumps({
    "query": {
        "term" : { "_id" : doc_id }
    }
})

for index in index_list:
    url = elastic_link_template.format(index)
    response = requests.get(url, data=query)
    results = json.loads(response.text)
    array = results["hits"]["hits"]
    if len(array) > 0:
        status = array[0]["_source"]["status"]
        print("Find doc ", doc_id, " in ", index, ", status: ", status)
    else:
        print("Doc not exist in ", index)

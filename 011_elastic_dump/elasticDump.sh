#!/bin/bash

#************************************************
#      Filename: elasticDump.sh
#        Author: wangshuguang - buaa_wsg@163.com
#   Description: ---
#       Created: 2018-06-06 10:49:38
# Last Modified: 2018-06-15 11:46:05
#************************************************
# input/output标准格式 [address]/[index]/[type] 可不指定type
input_address="http://xx.xxx.xxx.xxx:9200"
input_index="index_name"

output_address="http://xx.xxx.xxx.xxx:9200"
output_index="index_name"

# 每次传输多少个
trans_cnt_limit=100

#elasticdump \
#    --input=${input_address}/${input_index} \
#    --output=${output_address}/${output_index} \
#    --type=analyzer \
#elasticdump \
#    --input=${input_address}/${input_index} \
#    --output=${output_address}/${output_index} \
#    --type=mapping \
elasticdump \
    --input=${input_address}/${input_index} \
    --output=${output_address}/${output_index} \
    --type=data \
    --limit=${trans_cnt_limit} \
    --debug=false \
    --ignore-error=true \
    --maxSockets=3 > elasticdump.log 2>&1 &

# 2016/6/6 遇到一个问题就是130万的库导入到110万时候命令崩了
# Error: read ECONNRESET
# 我调大了maxSockets = 3 之前是2, 单个请求的doc数量从50升到100
# 然后成功导入了

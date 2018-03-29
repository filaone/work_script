#!/bin/bash

#************************************************
#      Filename: static_words.sh
#        Author: wangshuguang - buaa_wsg@163.com
#   Description: ---
#       Created: 2018-03-13 15:11:20
# Last Modified: 2018-03-13 15:22:15
#************************************************

[ $# -lt 1 ] && echo "Usage: basename $0 FILE WORDS" && exit -1

FILE=$1
((WORD_NUM=$#-1))
for n in  $(seq $WORD_NUM)
do
    # shift 是把第一参数往后移，第二个参数变成 $1
    shift
    cat $FILE | sed -e 's/[^a-zA-Z]/\'$'\n''/g' \
        | grep -v ^$ | sort | grep ^$1$ | uniq -c
done

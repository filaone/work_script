#!/usr/bin/env python
# -*- coding=utf8 -*-

#************************************************
#      Filename: pycurl.py
#        Author: wangshuguang - buaa_wsg@163.com
#   Description: ---
#       Created: 2018-03-29 16:33:43
# Last Modified: 2018-03-29 19:27:48
#************************************************/

import pycurl
import re
import os
from datetime import datetime
from time import sleep
import sys

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

def getConnectionTime(url, targetfile_handler):
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    #c.setopt(pycurl.WRITEDATA, targetfile_handler)
    try :
        c.perform()
        err_mess = ""
    except Exception as e :
        err_mess = str(e)

    print(err_mess)
    total_time = c.getinfo(pycurl.TOTAL_TIME)
    dns_time = c.getinfo(pycurl.NAMELOOKUP_TIME)
    connect_time = c.getinfo(pycurl.CONNECT_TIME)
    redirect_time = c.getinfo(pycurl.REDIRECT_TIME)
    ssl_time = c.getinfo(pycurl.APPCONNECT_TIME)
    pretrans_time = c.getinfo(pycurl.PRETRANSFER_TIME)
    starttrans_time = c.getinfo(pycurl.STARTTRANSFER_TIME)

    transfer_time = total_time - starttrans_time
    serverreq_time = starttrans_time - pretrans_time
    if ssl_time == 0 :
        if redirect_time == 0 :
            clientper_time = pretrans_time - connect_time
            redirect_time = 0
        else :
            clientper_time = pretrans_time - redirect_time
            redirect_time = redirect_time - connect_time
        ssl_time = 0
    else :
        clientper_time = pretrans_time - ssl_time
        if redirect_time == 0:
            ssl_time = ssl_time - connect_time
            redirect_time = 0
        else :
            ssl_time = ssl_time - redirect_time
            redirect_time = redirect_time - connect_time
    connect_time = connect_time - dns_time
    time_list = []
    time_list.append(floatToStr(dns_time))
    time_list.append(floatToStr(connect_time))
    time_list.append(floatToStr(redirect_time))
    time_list.append(floatToStr(clientper_time))
    time_list.append(floatToStr(serverreq_time))
    time_list.append(floatToStr(transfer_time))
    time_list.append(floatToStr(total_time))
    targetfile_handler.write("      ".join(time_list)+"\n")
    c.close()

def floatToStr(number):
   temp_number = float('%.1f'% float(number*1000))
   return str(temp_number)

def qpsController(qps_number):
   return float('%.2f' % float(1/int(qps_number)))

if __name__ == '__main__':
    commandFile = sys.argv[1]
    targetFile = "timeCollection."+datetime.now().strftime("%Y%m%d_%H%M%S")
    if not os.path.exists(targetFile):
        os.system(r'touch %s' % targetFile)
    targetFile_handler = open(targetFile, 'w')
    targetFile_handler.write("发起请求到DNS   TCP链接消耗时间    跳转消耗    SSL握手    客户端准备    服务器处理    传输时间    总耗时\n")
    if not os.path.exists(commandFile):
        print("请输入命令文件")
    commandFile_handler = open(commandFile, 'r')
    qps_number = sys.argv[2]
    time = qpsController(qps_number)
    for line in commandFile_handler:
        sleep(time)
        getConnectionTime(line.strip(), targetFile_handler)         
    print("时间排序:")    
    print("  1. 发起请求到DNS时间")    
    print("  2. TCP连接消耗时间")    
    print("  3. 跳转消耗时间")    
    print("  4. SSL握手时间")    
    print("  5. 客户端准备时间")    
    print("  6. 服务器处理时间")
    print("  7. 传输时间")
    print("  8. 总耗时")
    


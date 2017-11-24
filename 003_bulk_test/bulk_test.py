#!/usr/bin/python
#-*- coding:utf-8 -*-

import requests
import re
import os
import time
from optparse import OptionParser

def getQueryGroup(SRC_FILE, REQUEST_FILE, querytype, target):
	lineCount = 0
	if os.path.exists(REQUEST_FILE):
		print(os.popen('wc -l ' + REQUEST_FILE).readline())
		lineCount = int(os.popen('wc -l ' + REQUEST_FILE).readline().split()[0])
		print("REQUEST_FILE has been perpared.... : " + REQUEST_FILE)
		print(REQUEST_FILE + " lineCount = " + str(lineCount))
		return lineCount
	src_file = open(SRC_FILE,'r')
	req_file = open(REQUEST_FILE, 'w')
    # create pattern
	if querytype=='search':
		pattern = re.compile(r'.*ACCESS.*/service/search.*')
	elif querytype=='match':
		pattern = re.compile(r'.*ACCESS.*/service/match.*')
	else:
		pattern = re.compile(r'.*ACCESS.*/service/(search|match).*')
	
	for line in src_file:
		if pattern.match(line) is not None:
			request = line.split()[6]
			req_file.write('http://' + target + request + '&useCache=false\n')
			lineCount += 1
	req_file.flush()
	req_file.close()
	src_file.close()
	print("REQUEST_FILE has been perpared.... : " + REQUEST_FILE)
	print(REQUEST_FILE + " lineCount = " + str(lineCount))
	return lineCount


def bulkRequests(REQUEST_FILE, lineCount, throughput, sleepTime):
	req_file = open(REQUEST_FILE,'r')
	if  throughput > lineCount:
		throughput = lineCount
	for i in range(1,throughput):
		time.sleep(sleepTime)
		line = req_file.readline();
		requests.get(line)
	req_file.close()


def statistic_concurrent(FINAL_LOG, RESULT_FILE):
	costTime = 0
	docDaoCount = 0
	taskCount = 0
	idReqCount = 0
	idRecCount = 0
	result = []
	final_log = open(FINAL_LOG)

	pattern_task = re.compile(r'.*Invoke all the.*tasks in the DocDAO.*')
	pattern_time = re.compile(r'.*documents from thrift and mongo.*')
	for line in final_log:
		if pattern_task.match(line) is not None:
			docDaoCount += 1
			taskCount += int(line.split()[8])
		if pattern_time.match(line) is not None:
			tmp_list = line.split()
			costTime += float(tmp_list[-2])
			result.append(int(float(tmp_list[-2])))
			idReqCount += int(tmp_list[6].split('/')[1])
			idRecCount += int(tmp_list[6].split('/')[0])
	top = sorted(result)
	print(top[-100:])

	print("The Result: Total docDao REQUEST is "+str(docDaoCount)+", Task Count of REQUEST is "+str(taskCount))
	print("Cost time "+str(costTime)+"ms, RRetrieved "+str(idRecCount)+"/"+str(idReqCount)+" document\n")
	res_file = open(RESULT_FILE,'a')
	res_file.write(str(time.ctime()))
	res_file.write("The Result: Total docDao REQUEST is "+str(docDaoCount)+", Task Count of REQUEST is "+str(taskCount))
	res_file.write("Cost time "+str(costTime)+"ms, RRetrieved "+str(idRecCount)+"/"+str(idReqCount)+" document\n")
	res_file.write("top 100 cost time : " + str(top[-100:]))
	


parser = OptionParser()
parser.add_option("-t", "--target", dest="targetIp",
		help="please input the target ip 10.10.111.12:8035",
		default="10.101.2.17:8035")
parser.add_option("-q", "--qps", dest="qps",
		help="please input the query per second number(qps)",default=25)
parser.add_option("-T", "--throughput", dest="throughput",
		help="input the max throughput number", default=5000)
parser.add_option("-s", "--src_log", dest="srclog",
		help="a log file where to get the search query",
		default="./ServerLog/origin_log/worker-8035.log")
parser.add_option("-Q", "--query_type", dest="querytype",
		help="select the query type search/match/all of them",
		default="search")
(options, args) = parser.parse_args()

# please Make Sure These two files right
SRC_FILE=options.srclog      #where to get the search query
#FINAL_LOG=options.finallog  # where to get the log file
target = options.targetIp
throughput = int(options.throughput)
querytype = options.querytype

SRC_FILENAME=SRC_FILE.split('/')[-1]
REQUEST_FILE='./ServerLog/tmp_log/'+'tmp-'+ querytype + "-" + SRC_FILENAME
RESULT_FILE='./Result/'+'res-'+SRC_FILENAME

sleepTime = float(1/int(options.qps))

print("--------------------------------------------------------------")
print("  destIP     : " + options.targetIp)
print("  throughput : " + str(options.throughput))
print("  src_log    : " + options.srclog)
print("  query type : " + options.querytype)
print("  QPS        : " + str(options.qps))
print("  Req_File   : " + REQUEST_FILE)
print("  Res_File   : " + RESULT_FILE)
print("--------------------------------------------------------------")

# Create search query group by SRC_FILE (log file from searcher)
lineCount = getQueryGroup(SRC_FILE, REQUEST_FILE, querytype, target)
# send bulk request with a specific qps
bulkRequests(REQUEST_FILE, lineCount, throughput, sleepTime)
# Analysis the log of the server
#statistic_concorrent(FINAL_LOG, RESULT_FILE)



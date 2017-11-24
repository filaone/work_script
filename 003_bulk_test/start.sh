#/bin/bash

#Usage: bulk_test.py [options]
#
#Options:
#  -h, --help            show this help message and exit
#  -t TARGETIP, --target=TARGETIP
#                        please input the target ip 10.10.111.12:8035
#  -q QPS, --qps=QPS     please input the query per second number(qps)
#  -T THROUGHPUT, --throughput=THROUGHPUT
#                        input the max throughput number
#  -s SRCLOG, --src_log=SRCLOG
#                        a log file where to get the search query
#  -Q QUERYTYPE, --query_type=QUERYTYPE
#                        select the query type search/match/all of them

TARGET_IP="10.111.0.54:8041"
THROUGHPUT=5
SRCLOG="./ServerLog/origin_log/log.6"
QPS=1                           
OWNLOG="/home/services/wangshuguang/bulk_test/Logs/bt_test.log"
QUERYTYPE="match"


if [ ! -f "${OWNLOG}" ]; then
	touch "$OWNLOG"
fi

echo `date +%y/%m/%d--%H:%M:%S`" execute bulk test" >> ${OWNLOG}
nohup python bulk_test.py  -t ${TARGET_IP} -T ${THROUGHPUT} -s ${SRCLOG}  -q ${QPS} -Q ${QUERYTYPE}>> ${OWNLOG} 2>&1 &
#echo "Job done in "`date +%y/%m/%d--%H:%M:%S`

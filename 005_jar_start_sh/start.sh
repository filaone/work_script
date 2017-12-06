#!/bin/bash

HOME=./
JAVA_OPTS="-Xms1G -Xmx1G"
JAVA_OPTS="$JAVA_OPTS -XX:+PrintGCDetails"
JAVA_OPTS="$JAVA_OPTS -XX:+UseG1GC"
JAVA_OPTS="$JAVA_OPTS -XX:+PrintGCTimeStamps"
JAVA_OPTS="$JAVA_OPTS -XX:+PrintGCDateStamps"
JAVA_OPTS="$JAVA_OPTS -XX:+PrintClassHistogram"
JAVA_OPTS="$JAVA_OPTS -XX:+PrintTenuringDistribution"
JAVA_OPTS="$JAVA_OPTS -XX:+PrintGCApplicationStoppedTime"




nohup /home/services/jdk1.8.0_45/bin/java -agentlib:jdwp=transport=dt_socket,\
server=y,suspend=n,address=38046 -Dcom.sun.management.jmxremote.port=8046 \
-Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false\
$JAVA_OPTS -cp abc.jar com.yidian.cha.abc  &

echo $! > $HOME/var/abc.pid
echo $! > abc.pid

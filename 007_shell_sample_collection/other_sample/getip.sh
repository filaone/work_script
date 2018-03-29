#!/bin/bash

#************************************************
#      Filename: getip.sh
#        Author: wangshuguang - buaa_wsg@163.com
#   Description: get an usable ipaddress automatically
#		 实现一个dhcp的过程
#       Created: 2018-03-13 11:45:51
# Last Modified: 2018-03-13 12:17:00
#************************************************

net="192.168.1"
default_mask="192.168.1.1"
over_time=2


# check the default current ipaddress
# -c count -W wait_time
ping -c 1 $default_mask -W $over_time
# [ $? -eq 0 ] && echo "the current ipadress is okey!" && exit -1;

while :;
do
    # clear the current configuration
    # ifconfig eth0 down
    # configure the ip address of eth0
    #ifconfig eth0 \ 
    #$net.$(($RANDOM/130 +2)) \
    #up
    # configure the default gateway
    # route add default gw $default_gateway
    ping -c 1 $default_mask -W $over_time
    # if work, finish
    [ $? -eq 0 ] && echo "the ip is done!" && break
done



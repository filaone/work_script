#!/bin/bash
DOCKER_NUMBER=$1
MODULE_NAME=your-module-name
env=start-env
port=8888

# 准备 Container
image_name=docker-address:5000/publish/${MODULE_NAME}-master-${DOCKER_NUMBER}-image
docker pull ${image_name}
# 准备外部 _logs 目录
log_path=~/_logs/${MODULE_NAME}-${env}-
mkdir -p ${log_path}
# 清除已有的同名container
container_name=${MODULE_NAME}-${env}
docker stop ${container_name} && docker rm -f ${container_name}
# 准备启动项
local_ip=`ifconfig| grep "inet" | grep -v "inet6" | grep -v "127.0.0.1" | grep -v "broadcast 0.0.0.0" | awk '{print $2}'` | tee
container_start_cmd="/bin/bash -c \"cd /home/services/${MODULE_NAME}/bin/ && sh restart.sh ${env}\""
DOCKER_RUN_OPT=" -d
  -e CORP_LOCAL_IP=${local_ip}
  -e CORP_LOCAL_PORT=
  -e ORIGIN_SERVICE_PORT=${port}
  -e LANG=en_US.UTF-8
  -e TZ=Asia/Shanghai
  --name ${MODULE_NAME}-${env}
  -v ${log_path}:/home/services/${MODULE_NAME}/logs
  -v ${log_path}:/home/services/${MODULE_NAME}/bin/logs
  --net=host
  -p ${port}:${port}
  ${image_name}
  ${container_start_cmd};"

#启动docker
docker_cmd="docker run "${DOCKER_RUN_OPT}
echo "docker command : "${docker_cmd}
echo ${docker_cmd} | sh

#!/bin/bash
port=$1
echo $(netstat -tun | grep ${port}  | wc -l)

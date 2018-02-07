#!/bin/bash
for i in {1..3}
do
    sh ./slave.sh 512 2097152
    sh ./slave.sh 4k 262144
    sh ./slave.sh 64k 16384
    sh ./slave.sh 128k 8192
    sh ./slave.sh 512k 2048
    sh ./slave.sh 1M 1024
    sh ./slave.sh 4M 256
    sh ./slave.sh 64M 16
    sh ./slave.sh 128M 8
    sh ./slave.sh 512M 2
    sh ./slave.sh 1G 1
done

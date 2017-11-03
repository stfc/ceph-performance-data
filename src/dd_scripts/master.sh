#!/bin/bash
for i in {1..10}
do
    sh ./slave.sh 4K
    sh ./slave.sh 64K
    sh ./slave.sh 128K
    sh ./slave.sh 512K
    sh ./slave.sh 1M
    sh ./slave.sh 4M
    sh ./slave.sh 64M
    sh ./slave.sh 128M
    sh ./slave.sh 512M
    sh ./slave.sh 1G
done

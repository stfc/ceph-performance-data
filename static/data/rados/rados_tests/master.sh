#!bin/bash

for i in {1..1}
do
    sh ./slave.sh 60 1M
    sh ./slave.sh 60 2M
    sh ./slave.sh 60 4M
    sh ./slave.sh 60 8M
    sh ./slave.sh 60 16M
    sh ./slave.sh 60 32M
    sh ./slave.sh 60 64M
done

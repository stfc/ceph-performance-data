#!/bin/bash

DATE=$(date "+%Y-%m-%d %H:%M:%S")

wname="./logs/write_bs$1.log"
rname="./logs/read_bs$1.log"
uname="bs$1.log"

if [[ -e $wname ]] ; then
    i=2
    while [[ -e "./logs/write_bs$1-$i.log" ]] ; do
        let i++
    done
    wname="./logs/write_bs$1-$i.log"
fi

if [[ -e $rname ]] ; then
    j=2
    while [[ -e "./logs/read_bs$1-$j.log" ]] ; do
        let j++
    done
    rname="./logs/read_bs$1-$j.log"
fi


echo "Time:$DATE" >> $wname
echo "Blocksize:$1" >> $wname
echo 3 > /proc/sys/vm/drop_caches
dd if=/dev/zero of=./tempfile bs="$1" count=1 oflag=direct >> $wname 2>&1

echo "Time:$DATE" >> $rname
echo "Blocksize:$1" >> $rname
echo 3 > /proc/sys/vm/drop_caches
dd if=./tempfile of=/dev/null bs="$1" count=1 status=progress >> $rname 2>&1

rm ./tempfile

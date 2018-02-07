#!/bin/bash

DATE=$(date "+%Y-%m-%d %H:%M:%S")
BS=$1
COUNT=$2
FOLDER="./logs/${BS}_bs_logs"

echo "Running Test $BS $COUNT"

if ! [ -e $FOLDER ] ; then
    mkdir $FOLDER
fi
wname="./$FOLDER/write_${BS}_${COUNT}.log"
rname="./$FOLDER/read_${BS}_${COUNT}.log"
uname="${BS}_${COUNT}.log"

if [[ -e $wname ]] ; then
    i=2
    while [[ -e "./$FOLDER/write_${BS}_${COUNT}-$i.log" ]] ; do
        let i++
    done
   wname="./$FOLDER/write_${BS}_${COUNT}-$i.log"
fi

if [[ -e $rname ]] ; then
    j=2
    while [[ -e "./$FOLDER/read_${BS}_${COUNT}-$j.log" ]] ; do
        let j++
    done
    rname="./$FOLDER/read_${BS}_${COUNT}-$j.log"
fi


echo "Time:$DATE" >> $wname
echo "Blocksize:$BS" >> $wname
echo "Count:$COUNT" >> $wname
echo 3 > /proc/sys/vm/drop_caches
dd if=/dev/zero of=./tempfile bs="$BS" count=$COUNT oflag=direct >> $wname 2>&1

echo "Time:$DATE" >> $rname
echo "Blocksize:$BS" >> $rname
echo "Count:$COUNT" >> $rname
echo 3 > /proc/sys/vm/drop_caches
dd if=./tempfile of=/dev/null bs="$BS" count=$COUNT status=progress >> $rname 2>&1

rm ./tempfile

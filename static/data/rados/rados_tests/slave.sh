DATE=$(date "+%Y-%m-%d %H:%M:%S")

wname="./logs/write_$1_$2.log"
rname="./logs/read_$1_$2.log"
uname="$1_$2"

# check if filename exists, and if so increment number (file.log, file-2.log...)
if [[ -e $wname ]] ; then
    i=2
    while [[ -e "./logs/write_$uname-$i.log" ]] ; do
        let i++
    done
    wname="./logs/write_$uname-$i.log"
fi

if [[ -e $rname ]] ; then
    j=2
    while [[ -e "./logs/read_$uname-$j.log" ]] ; do
        let j++
    done
    rname="./logs/read_$uname-$j.log"
fi


# drop caches before doing benchmark
echo 3 > /proc/sys/vm/drop_caches && sync

echo "Time:$DATE" >> $wname
echo "Duration(s):$1" >> $wname
echo "BlockSize(MB):$2" >> $wname

# run write benchmark
rados bench -p scbench -b $2 $1 write --no-cleanup >> $wname


# drop caches before doing benchmark
echo 3 > /proc/sys/vm/drop_caches && sync

echo "Time:$DATE" >> $rname
echo "Duration(s):$1" >> $rname
echo "BlockSize(MB):$2" >> $rname

# run read benchmark
rados bench -p scbench $1 rand >> $rname

# clean up
rados -p scbench cleanup --prefix benchmark_data

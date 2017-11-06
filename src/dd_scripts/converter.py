import sys
import os
import csv

# This script is very much hacked together
# and wont work if dd count is more than 1


#----------------------------------------------\n
#Time: 2017-11-01 10:59:00
#Blocksize: 4K
#1+0 records in
#1+0 records out
#4096 bytes (4.1 kB) copied, 0.000472967 s, 8.7 MB/s

ttype  = sys.argv[1]
logpath = sys.argv[2]
outputfile = sys.argv[3]

logfiles = os.listdir(logpath)

data = []

for lf in logfiles:
    if lf.startswith(ttype) == False:
        continue

    entry = {}
    print 'opening log ' + logpath + '/' + lf
    f = open(logpath+'/'+lf, 'r')
    
    ts = f.readline()[5:]
    ts = ts.replace('\n', '')
    entry["TimeStamp"] = ts

    bs = f.readline().split(':')[1]
    bs = bs.replace('\n', '')
    bs_unit = bs[-1]
    bs = bs[:-1]
    if bs_unit == 'M':
        bs = int(bs) * 1024
    elif bs_unit == 'G':
        bs = int(bs) * 1024 * 1204

    entry["BlockSize(K)"] = bs
    
    while f.readline() != '1+0 records in\n':
       pass

    f.readline() # discard another line

    line = f.readline()
    metrics = line.split(',')
    size_m = metrics[0]
    time_m = metrics[1]
    speed_m = metrics[2]
        
    size = size_m.split(' ')[0]
    time = time_m.split(' ')[1]
    speed = speed_m.split(' ')[1]
    units = speed_m.split(' ')[2]
    if units == 'GB/s\n':
        speed = float(speed) * int(1024)
    if units == 'Kb/s\n':
        speed = float(speed) / int(1024)
    speed = str(speed)
    speed = speed.replace('\n', '')
    entry["Bytes"] = size
    entry["Time(s)"] = time
    entry["TransferRate(MB/s)"] = speed
    data.append(entry)
    f.close()


outf = open(outputfile, 'w+')
w = csv.DictWriter(outf, ["BlockSize(K)","Bytes", "Time(s)", "TransferRate(MB/s)", "TimeStamp"], lineterminator='\n')
w.writeheader()
w.writerows(data)

outf.close()



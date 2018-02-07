import sys
import os
import csv

# This script is very much hacked together

ttype  = sys.argv[1]
logpath = sys.argv[2]
outputfile = sys.argv[3]

logfiles = os.listdir(logpath)

data = []

for lf in logfiles:
    if lf.startswith(ttype) == False:
        continue

    entry = {}
    f = open(logpath+'/'+lf, 'r')
    
    ts = f.readline()[5:]
    ts = ts.replace('\n', '')
    entry["TimeStamp"] = ts

    bs = f.readline().split(':')[1]
    bs = bs.replace('\n', '')

    entry["BlockSize"] = bs
    if isinstance(bs[:-1], int) == False:
        bs = bs[:-1]
    
    count = f.readline().split(':')[1]
    count.replace('\n', '')
    entry["FileSize"] = int(bs) * int(count)
    
    # get last line
    temp_line = f.readline()
    line = ""
    while temp_line != "":
        temp_line = f.readline()
        if temp_line != "":
            line = temp_line
    
    print "last line: " + line
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
   # entry["Bytes"] = size
    entry["Time(s)"] = time
    entry["TransferRate(MB/s)"] = speed
    data.append(entry)
    f.close()

outf = open(outputfile, 'w+')
w = csv.DictWriter(outf, ["BlockSize","FileSize", "Time(s)", "TransferRate(MB/s)", "TimeStamp"], lineterminator='\n')
w.writeheader()
w.writerows(data)

outf.close()

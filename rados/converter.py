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
columns = []
for lf in logfiles:
    if lf.startswith(ttype) == False:
        continue

    entry = {}
    f = open(logpath+'/'+lf, 'r')
    
    ts = f.readline()[5:]
    ts = ts.replace('\n', '')
    entry["TimeStamp"] = ts

    dur = f.readline().split(':')[1]
    dur = dur.replace('\n', '')
    entry["Duration(s)"] = dur 
    
    bs = f.readline().split(':')[1]
    bs = bs.replace('\n', '')
    bs_unit = bs[-1]
    bs = bs[:-1]
    if bs_unit == 'M':
        bs = int(bs) * 1024
    elif bs_unit == 'G':
        bs = int(bs) * 1024 * 1204

    entry["BlockSize(K)"] = bs
    
    # Total time run:       600.285683
    line = f.readline() 
    while line.split(':')[0] != 'Total time run':
	line = f.readline()
        pass

    # replace previously set duration with more accurate one
    dur = line.split(':')[1]
    dur = dur.replace(' ', '')
    dur = dur.replace('\n', '')
    entry["Duration(s)"] = dur

    # loop over the rest, dont bother with formatting
    line = f.readline()
    while line != '':
        field = line.split(':')[0]
        val = line.split(':')[1]
        val = val.replace(' ', '').replace('\n', '')
        entry[field] = val
        line = f.readline()
    
    if not columns:
        for k in entry:
            columns.append(k)

    data.append(entry)
    f.close()

outf = open(outputfile, 'w+')
w = csv.DictWriter(outf, columns, lineterminator='\n')
w.writeheader()
w.writerows(data)

outf.close()


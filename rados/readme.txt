The data is in the ./logs folder, for every run there is a 'read' and 'write' test.

There three scripts that help with automation. The 'master.sh' and 'slave.sh' scripts automata the rados tests.
While the 'converter.py' script converts the data into CSV files.

-----------------------
------ master.sh-------
-----------------------
master.sh does not take any command line arguments, the file contains a simple for loop with a number of calls to slave.sh
The number of repeats can be changed by modifying the number of times the for loop runs.
By changing the calls to the slave scripts, the number of tests and their content can be changed.



-----------------------
------ slave.sh-------
-----------------------
The slave scipt takes two argument, the duration and blocksize arguments as specified by rados-bench.
The script writes to folder called 'logs'.
The script writes the logs to files with following format: './logs/<write or read>_<duration>_<blocksize>.log
In the case that tests are repeated, the script checks if the file exists, and if so will incrementally append a number to the end, e.g. file-1,file-2 etc


---------------------------
------ converter.py -------
---------------------------
This script converts the .log files into CSV format.
Script takes three arguments, the IO type (write or read), the filepath to the logs and the filepath to the output file.
	ttype: the IO type (write or read)
	logpath: the filepath to the logs, if this folder has not been changed it will be ./logs
	outputfile : the output file, e.g.  ./logs/write.csvs

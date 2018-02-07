The data is in the ./logs folder, each run has its own folder. Within it are the original logs of the dd runs, these end in the '.log' prefix.
The folders also contain a 'read.csv' and 'write.csv' file. These contain the data for the appropiate I/O type formatted as CSV files.

There three scripts that help with automation. The 'master.sh' and 'slave.sh' scripts automata the dd tests.
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
The slave scipt takes two argument, the blocksize and count arguments as specified by dd.
The script writes to folder called 'logs' which is hardcoded, but can be changed easily (its a variable FOLDER at the top of the script).
For every blocksize and count combination a  new folder is created in './logs' where the data is written too.
The script writes the logs to files with following format: './logs/<blocksize>_bs_logs/<write or read>_<blocksize>_<count>.log
In the case that tests are repeated, the script checks if the file exists, and if so will incrementally append a number to the end, e.g. file-1,file-2 etc


---------------------------
------ converter.py -------
---------------------------
This script converts the .log files into CSV format.
This script is not very stables, in works fine with the current configuration of the tests, but should the dd tests change, this may or may not work.
Script takes three arguments, the IO type (write or read), the filepath to the logs and the filepath to the output file.
	ttype: the IO type (write or read)
	logpath: the filepath to the log, if this folder has not been changed it will be ./logs/<test run> e.g. ./logs/128k_bs_logs/
	outputfile : the output file, e.g.  ./logs/128k_bs_logs/write.csv

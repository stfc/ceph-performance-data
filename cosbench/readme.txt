The archives folder contains the original cosbench output. The formatted folder contains formatted into JSON by the python scripts.
There are multiple CSV files for every COSBench fun, one for every stage and an overview one. 
As an example looking at workload 45 in ./archive/w450-4KB we are a large list of CSV files for every stage. 
The CSV file containing an overview of the run as a whole is 'w45-4KB.csv'. All COSBench runs follow the same format.
<stage>-<name>.csv

The python script (convert_cosbench_tests.py) will format all the raw data into JSON for ease of use with visualisation tools.
The script takes the following arguments:
	archive_filepath : Filepath to the folder containing the COSBench data. If this folder has not been changed it is ./archive
	replace_flag : 'True' or 'False', flag to replace the existing formatted data.
	output_directory : Filepath to the directory formatted data should be output to.

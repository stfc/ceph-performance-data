import sys
import os
import shutil
import csv
import xml.etree.ElementTree as ET
import json
import re



# -------------------------------------------------------------------
# ---------------------- GLOBAL VARIABLES ---------------------------
# -------------------------------------------------------------------

# Archive Filepath for the cosbench data
archive_filepath = ""

# Flag to replace existing converted data
replace_flag = False

# Directory to output conversion
output_directory = ""




# -------------------------------------------------------------------
# ----------------------- FUNCTIONS ---------------------------------
# -------------------------------------------------------------------


def generate_json(workload_filepath):
    data_dict = {}
    
    # extract workload ID from filepath
    data_dict['id'] = get_id(workload_filepath)        
    data_dict['title'] = 'Workload ' + data_dict['id']

    # get xml attributes (endpoint, storage, workers
    xml_data = parse_xml(workload_filepath)
    for e in xml_data:
        data_dict[e] = xml_data[e]
    
    # get summary data
    cols, data = get_summary_data(workload_filepath)
    data_dict['columns'] = cols 
    data_dict['data'] = data
    
    # convert to json
    json_string = json.dumps(data_dict, indent=4, sort_keys=True)
    return json_string


# ----------------------- Utility Function -------------------------
def get_id(workload_filepath):
    regx = re.compile('w[0-9]+')
    return regx.match(workload_filepath).group(0)


def parse_xml(workload_filepath):
    xml_dict = {}
    config_xml_tree = ET.parse(archive_filepath + '/' + workload_filepath + '/workload-config.xml')
    root = config_xml_tree.getroot()
    for element in root:
        if element.tag == 'storage':
            config = element.get('config')
            for val in config.split(';'):
                if val.split('=')[0] == 'endpoint':
                    xml_dict['endpoint'] = val.split('=')[1]
            xml_dict['storage_type'] = element.get('type')
        if element.tag == 'workflow':
            for stage in element:    
                if stage.tag == 'workstage' and stage.get('name') == 'main':
                    for child in stage:
                        if child.tag == 'work' and child.get('name') == 'main':
                            xml_dict['workers'] = int(child.get('workers'))
    return xml_dict
                   

def pretty_print_dict(data):
    for e in data:
        print e, data[e]

# Stage,Op-Name,Op-Type,Op-Count,Byte-Count,Avg-ResTime,Avg-ProcTime,60%-ResTime,80%-ResTime,90%-ResTime,95%-ResTime,99%-ResTime,100%-ResTime,Throughput,Bandwidth,Succ-Ratio,Status,Detailed Status
def get_summary_data(workload_filepath):
    summary_arr = []
    with open(archive_filepath+'/'+workload_filepath+'/'+workload_filepath+'.csv') as f:
        reader = csv.reader(f)
        col_header = reader.next() # gives the index of the actual position of columns in row

        # only extract these columns
        columns = ['Stage','Op-Type','Op-Count','Byte-Count','Avg-ResTime','Avg-ProcTime',
                            'Throughput','Bandwidth','Succ-Ratio','Status']
        for row in reader:
            #if row[0] != 's3-main': continue
            entry = {}
            for col in columns:
                try:
                    entry[col] = float(row[col_header.index(col)])
                except ValueError:
                    entry[col] = row[col_header.index(col)]
                #entry['Op-Type'] = row[columns.index('Op-Type')]
                #entry['Op-Count'] = float(row[columns.index('Op-Count')])
                #entry['Byte-Count'] = float(row[columns.index('Byte-Count')])
                #entry['Avg-ResTime'] = float(row[columns.index('Avg-ResTime')])
                #entry['Avg-ProcTime'] = float(row[columns.index('Avg-ProcTime')])
                #entry['Throughput'] = float(row[columns.index('Throughput')])
                #entry['Bandwidth'] = float(row[columns.index('Bandwidth')])
                #entry['Succ-Ratio'] = float(row[columns.index('Succ-Ratio')].strip('%'))
                #entry['Status'] = row[columns.index('Status')]
            summary_arr.append(entry)
                             
    return (columns, summary_arr)

#def get_detailed_data(workload_filepath):
    
    
# -------------------------------------------------------------------
# ----------------------- ENTRY POINT -------------------------------
# -------------------------------------------------------------------


archive_filepath = sys.argv[1]
replace_flag = sys.argv[2] == 'True'
output_directory = sys.argv[3]

# Loop over the archives folder
for workload_filepath in os.listdir(archive_filepath):
    reg_match = re.compile('w[0-9]+').match(workload_filepath)
    if reg_match != None:
        id = reg_match.group(0)

        # check if directory already exists
        workload_dir = output_directory+'/'+id
        if os.path.exists(workload_dir) and not replace_flag:
            continue
        
        # create directory for workload
        if not os.path.exists(workload_dir):
            os.makedirs(workload_dir)
        
        # write json
        json_string = generate_json(workload_filepath)
        print json_string
        json_file = open(workload_dir+'/data.json', 'w+')
        json_file.write(json_string)

        # copy over config file
        shutil.copyfile(archive_filepath+'/'+workload_filepath+'/workload-config.xml', workload_dir+'/config.xml')      


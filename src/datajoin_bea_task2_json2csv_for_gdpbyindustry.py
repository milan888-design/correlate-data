#test convert json into table.py
import json
import prettytable
from jsonpath_ng import parse
import logging
from prettytable import PrettyTable

# read json file and assign to a variable
file1src = open('generic_fileseed1.txt', "r")
fileseed1=file1src.read()

src_filename=fileseed1+".json"
# read json file and assign to a variable
file1src = open(src_filename, "r")
file1textsrc=file1src.read()
#define dictionary for source file data
src=dict()
#load source file data in disctionary
src= json.loads(file1textsrc)
#print(src)
#x=prettytable.PrettyTable(["TableID","Frequency","Year","Quarter","Industry","IndustrYDescription","DataValue","NoteRef"])

json_data = json.loads(file1textsrc)

# Create a PrettyTable object and add some data
table1 = PrettyTable()
table1.field_names = ["TableID","Frequency","Year","Quarter","Industry","IndustrYDescription","DataValue","NoteRef"]

for item in src:
    TableID=item["TableID"]
    Frequency=item["Frequency"]
    Year=item["Year"]
    Quarter=item["Quarter"]
    Industry=item["Industry"]
    IndustrYDescription=item["IndustrYDescription"]
    DataValue=item["DataValue"]
    NoteRef=item["NoteRef"]
    table1.add_row([TableID,Frequency,Year,Quarter,Industry,IndustrYDescription,DataValue,NoteRef])

# Export the table to a CSV file
with open(fileseed1+'.csv', 'w', newline='') as csvfile:
    csvfile.write(table1.get_csv_string())

print("CSV file created successfully!")


# Configure logging
logging.basicConfig(
    filename='datajoin_bea_task2_json2csv_for_template3.log',  # Log file name
    level=logging.ERROR,       # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)
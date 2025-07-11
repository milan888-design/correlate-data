import pandas as pd
from sqlalchemy import MetaData, create_engine, Table
import logging
# read json file and assign to a variable
#file1src = open('generic_fileseed1.txt', "r")
#fileseed1=file1src.read()
#fileseed1='economy_gdp'
#fileseed1='crime_hate'
#fileseed1='state_name'
#fileseed1='year_name'
#filename='customer'
#filename='sales_order_shipto_address'
#filename='sales_order'
#filename='order_type'
#filename='product_type'
#filename='address'
#filename='st_role'
#filename='st_role_user'
#filename='st_object'
#filename='st_role_object'
#filename='test_table'
#filename='st_role_object_operation'
#filename='wf_workflow'
#filename='wf_workflow_step'
#filename='wf_workflow_step_attribute'
#filename='st_object_extension_v2'
#filename='ds_program_parameter'
#filename='gdp_by_county_state_year'
filename='sales_by_county_state_year'
#filename='sales_order'
#foldername='C:/Users/milan/OneDrive/sdna_products/draft/'
foldername='C:/git/correlate-data/src/'
#dbname='testgraphquery'
#dbname='test_rbac'
#dbname='test_workflow'
#dbname='testapp1'
dbname='test_correlate'
# Load the CSV files
#df = pd.read_csv(fileseed1+'_new.csv')
#df = pd.read_csv(fileseed1+'_new.csv', dtype=str)
#df = pd.read_csv('C:/Users/milan/OneDrive/sdna_projects_2017onward/DataJoin/table_name_sum_scale_sql.csv', dtype=str)
#df = pd.read_csv('C:/Users/milan/OneDrive/sdna_projects_2017onward/alm/workflow_template2_3.csv', dtype=str)
df = pd.read_csv(foldername+filename+'.csv', dtype=str)
# Create a connection to the database 
#engine = create_engine('postgresql://postgres:Welcome123@localhost:5432/datajoin')  
#engine2 = create_engine('postgresql://postgres:Welcome123@localhost:5432/datasum')  
#engine = create_engine('postgresql://postgres:Welcome123@localhost:5432/alm')  
engine = create_engine('postgresql://postgres:Welcome123@localhost:5432/'+dbname) 
# Replace with your database connection string

# Define the table name
#table_name = fileseed1
#table_name = "workflow_template1"
#table_name = "workflow_template2_3"
table_name = filename

# Upload the DataFrame to the SQL table
df.to_sql(table_name, engine, index=False, if_exists='replace')
#comment out the following if datasum tables are different from datajoin
#df.to_sql(table_name, engine2, index=False, if_exists='replace')

# Verify the data has been uploaded
result = pd.read_sql(f"SELECT * FROM {table_name}", engine)
print(result)

# Create an engine and connect to the database
#engine = create_engine('postgresql://postgres:Welcome123@localhost:5432/datajoin')  
#engine = create_engine('postgresql://postgres:Welcome123@localhost:5432/datasum')  
#engine = create_engine('postgresql://postgres:Welcome123@localhost:5432/alm') 
engine = create_engine('postgresql://postgres:Welcome123@localhost:5432/'+dbname) 
# Replace with your database connection string
connection = engine.connect()

# Load the table metadata
metadata = MetaData()
metadata.reflect(bind=engine)
table = Table(table_name, metadata, autoload_with=engine)
#table = Table('new_table', metadata, autoload=True, autoload_with=engine)
#table = Table('new_table', metadata, autoload=True)
# Read column names
columns = [column.name for column in table.columns]

# Print column names
print("Columns in the table:")
for col in columns:
    print(col)

# Optional: Querying the table
#result = connection.execute(table.select()).fetchall()
#for row in result:
#    print(row)
# Retrieve column data types
column_types = {column.name: column.type for column in table.columns}

# Print column data types
print("Column data types in the table:")
for column_name, column_type in column_types.items():
    print(f"{column_name}: {column_type}")
    
# Close the connection
connection.close()

# Configure logging
#logging.basicConfig(
#    filename='datajoin_generic_task5createtable_log.log',  # Log file name
#    level=logging.ERROR,       # Log level
#    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
#)
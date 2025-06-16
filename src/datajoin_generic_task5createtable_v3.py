import pandas as pd
from sqlalchemy import MetaData, create_engine, Table
import sys 
from datetime import datetime
# read json file and assign to a variable
if __name__ == '__main__':
	arg1_table_name=sys.argv[1]
	arg2_targetserver=sys.argv[2]
	arg3_targetdb=sys.argv[3]
	arg4_inputfilefolder=sys.argv[4]
	arg5_inputfile= sys.argv[5]
 
#open log file
file1log = open(arg4_inputfilefolder +'datajoin_createtable_log.txt', 'a')
file1log.writelines("------"+'\n')
file1log.writelines(str(datetime.now())+"-start for-"+arg5_inputfile+'\n')

df = pd.read_csv(arg4_inputfilefolder +arg5_inputfile, dtype=str)
engine = create_engine(arg3_targetdb)  
df.to_sql(arg1_table_name, engine, index=False, if_exists='replace')

file1log.writelines(str(datetime.now())+"-end process for-"+arg5_inputfile+'\n')
file1log.writelines("======"+'\n')
file1log.close()
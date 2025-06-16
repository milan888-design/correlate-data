#from numpy import double, float64
import pandas as pd
from sqlalchemy import MetaData, create_engine, Table
from mlxtend.preprocessing import minmax_scaling
import logging
import sys 
from datetime import datetime
if __name__ == '__main__':
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    arg4 = sys.argv[4]
    arg5 = sys.argv[5]
    arg6 = sys.argv[6]

#C:\Users\milan\AppData\Local\Programs\Python\Python311\python.exe
#arg0 is the file name, c:\pyfiles\datajoin_generic_task6sum_scale_v2.py
#arg1 is datajoin ecnonomy_gdp_by_industry
#arg2 is datasum ecnonomy_gdp_by_industry_summary
#arg3-is to be scaled columnname gdp
#arg4 is sql for sum select country_name~industr
#arg5 is dbconnection datajoin postgresql://postgres:PASS@localhost:5432/datajoin
#arg6 is dbconnection datasum postgresql://postgres:PASS@localhost:5432/datasum 
#arg4='select country_name~industry_description~year_name~currency~sum(cast(gdp as numeric(10~2))) as gdp from economy_gdp_by_industry group by country_name~industry_description~year_name~currency'
modified_string = arg4.replace("~", ",")

engine = create_engine(arg5)  
connection1 = engine.connect()
df = pd.read_sql_query(modified_string, connection1)
scaled_column=arg3
column_data = df[scaled_column].values
column_values = minmax_scaling(column_data, columns=[0])
dftemp = pd.DataFrame(column_values, columns=['scaled_column'])
dftemp['scaled_column'] = dftemp['scaled_column'].astype(float)
dftemp['scaled_column']=dftemp['scaled_column']*100
dftemp['scaled_column']=dftemp['scaled_column'].round(2)
df[scaled_column+'_scaled'] = dftemp['scaled_column']
engine2 = create_engine(arg6)  
df.to_sql(arg2, engine2, index=False, if_exists='replace')
connection1.close()

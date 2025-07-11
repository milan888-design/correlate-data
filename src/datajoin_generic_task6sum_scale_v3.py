from numpy import double, float64
import pandas as pd
from sqlalchemy import MetaData, create_engine, Table
from mlxtend.preprocessing import minmax_scaling
#for sales table
#arg1='sales_by_county_state_year'
#arg2='sales_by_county_state_year_summary'
#arg3='sales_in_thousand'
#arg4='select state,year,sum(cast(sales_in_thousand as numeric(10,1))) as sales_in_thousand from sales_by_county_state_year group by state,year'
#arg5='postgresql://postgres:pass@localhost:5432/test_correlate'
#arg6='postgresql://postgres:pass@localhost:5432/test_correlate'

#for gdp table
arg1='gdp_by_county_state_year'
arg2='gdp_by_county_state_year_summary'
arg3='gdp_in_thousand'
arg4='select state,year,sum(cast(gdp_in_thousand as numeric(10,1))) as gdp_in_thousand from gdp_by_county_state_year group by state,year'
arg5='postgresql://postgres:pass@localhost:5432/test_correlate'
arg6='postgresql://postgres:pass@localhost:5432/test_correlate'

modified_string = arg4.replace("~", ",")

engine = create_engine(arg5)  
connection1 = engine.connect()
df = pd.read_sql_query(modified_string, connection1)
scaled_column=arg3
column_data = df[scaled_column].values
column_values = minmax_scaling(column_data, columns=[0])
dftemp = pd.DataFrame(column_values, columns=['scaled_column'])
dftemp['scaled_column'] = dftemp['scaled_column'].astype(float64)
dftemp['scaled_column']=dftemp['scaled_column']*100
dftemp['scaled_column']=dftemp['scaled_column'].round(2)
df[scaled_column+'_scaled'] = dftemp['scaled_column']
engine2 = create_engine(arg6)  
df.to_sql(arg2, engine2, index=False, if_exists='replace')
connection1.close()
import pandas as pd
import sys 

if __name__ == '__main__':
	arg1_table_name=sys.argv[1]
	arg2_inputfilefolder=sys.argv[2]
	arg3_inputfile= sys.argv[3]
	arg4_column_name1= sys.argv[4]
	arg5_column_name2= sys.argv[5]
df1 = pd.read_csv(arg2_inputfilefolder+arg3_inputfile,dtype=str)
df1[arg5_column_name2] = df1[arg4_column_name1]

df1 = df1.astype(str)
df1.to_csv(arg2_inputfilefolder+arg3_inputfile, index=False)
#df1.to_csv(fileseed1+'_new.csv', dtype=str)

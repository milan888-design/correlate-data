import pandas as pd
import sys 

if __name__ == '__main__':
    arg1_table_name=sys.argv[1]
    arg2_inputfilefolder=sys.argv[2]
    arg3_inputfile1= sys.argv[3]
    arg4_column_name1= sys.argv[4]
    arg5_inputfilefolder2=sys.argv[5]
    arg6_inputfile2= sys.argv[6]
    arg7_column_name2= sys.argv[7]
    arg8_column_name3= sys.argv[8]  

csv_file_1 =arg2_inputfilefolder+arg3_inputfile1
csv_file_2 =arg5_inputfilefolder2+arg6_inputfile2
column_name_1 =arg4_column_name1
column_name_2 =arg7_column_name2

# Load the CSV files
main_df = pd.read_csv(csv_file_1, dtype=str)
main_df=main_df.astype(str)

# Select the column and convert it to a list
lookup_df = pd.read_csv(csv_file_2, dtype=str)
lookup_df =lookup_df.astype(str)
# Create a mapping dictionary from lookup_df
mapping_dict = dict(zip(lookup_df[arg7_column_name2], lookup_df[arg8_column_name3]))
# Replace values in main_df using the mapping dictionary
main_df[arg4_column_name1] = main_df[arg4_column_name1].replace(mapping_dict)

main_df=main_df.astype(str)
main_df.to_csv(csv_file_1, index=False)
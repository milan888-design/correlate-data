import requests
import logging
# read json file and assign to a variable
#file1src = open('generic_fileseed1.txt', "r")
#fileseed1=file1src.read()
#fileseed1='economy_unemployment_rate'
#fileseed1='Economy_GDP_by_state'
fileseed1='economy_gdp_by_industry'

url = "https://apps.bea.gov/api/data/"
params = {
    "UserID": "YOUR KEY",
    "method": "GetData",
    "DataSetName": "GDPbyIndustry",
    "Year": "2024,2023,2022,2021,2020",
    "Industry": "ALL",
    "tableID": "1",
    "Frequency": "A",
    "ResultFormat": "json",
    "jsonp": "MY_FUNCTION_NAME"
}

response = requests.get(url, params=params)

# Print the response content
#print(response.text)
with open(fileseed1+'.txt', 'w') as file:
    file.write(response.text)
#open text file. Look for data[]note and remove all before data and note on ward
#Thus only array of json records will be left
try:
    data = response.json()
    print(data)
except ValueError:
    print("Response content is not valid JSON")

# Check if the request was successful
#if response.status_code == 200:
    # Get the JSON response
#    data = response.json()
#    print(data)
#else:
#    print(f"Request failed with status code {response.status_code}")

# Configure logging
logging.basicConfig(
    filename='datajoin_bea_POST_template3_log.log',  # Log file name
    level=logging.ERROR,       # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)
from pathlib import Path
import requests
# import csv
import pandas as pd

# Import datetime module to delineate start and stop dates for historical data
import datetime
from datetime import timedelta

#import pandas as pd

# Test ticker for data retrieval saved to variable for api_url implementation
# ticker = 'AAPL'

def polygon_api(ticker, start_day_days):

    # Datetime modeul implemented to store start and stop dates in variable.
    # Variables will be input into the url to make the api call
    end = datetime.date.today()
    start = end - timedelta(days=start_day_days)

    # Key is stored in a variable and the url is made into an f string to make it modular for other inputs
    api = 'QKNWUEbzmzgOs4AtUbgMfGOr0SF1xqT4'
    api_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start}/{end}?apiKey={api}'

    # print(api_url)

    # Make api call and save the resulting data in a dataframe
    # Print the dataframe
    data = requests.get(api_url).json()
    df = pd.DataFrame(data['results'])
    return df

# Use pathlib for path maintainence and write dataframe to csv
#file = 'AAPL_2yo_hist_6_26_21.csv'
#path = f"C:\\Users\\jpmad\\OneDrive\\Desktop\\Columbia FinTech BootCamp\\Workspace\\Python_Project\\Practice_Projects\\{file}"

# csvpath = Path('AAPL_2yo_hist_6_26_21.csv')

# df.to_csv(csvpath)
# print("Writing dataframe to csv...")

#with open(csvpath, 'w', newline='') as csvfile:

#    csvwriter = csv.writer(csvfile)
#    for row in data:
#        csvwriter.writerow(row.values())
import pandas as pd
from pathlib import Path
import fire

import questionary
from polygon import polygon_api

# from check_ticker import check_ticker

# tickers_path = Path('../tickers.csv')

# tickers_df = pd.read_csv(tickers_path)
def _get_polygon_api_info():

    # Format ticker
    ticker = questionary.text("Enter a ticker to get its data: ").ask()
    ticker = ticker.upper()

    # Get historical data timeframe in length days
    days = questionary.text("Enter timefram in length days: ").ask()
    days = int(days)

    # Get dataframe for given ticker
    df = polygon_api(ticker, days)

    return df  

def _clean_columns(dataframe):
    dataframe.columns = ['volume','volume weighted','open','close','high','low','t','n']
    dataframe = dataframe.drop(columns=['t','n'], inplace=True)
    return dataframe

def run():
    df = _get_polygon_api_info()
    _clean_columns(df)
    print(df)

if __name__ == '__main__':
    fire.Fire(run)
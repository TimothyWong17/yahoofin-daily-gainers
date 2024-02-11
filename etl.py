import pandas as pd
import os
import re
import sqlite3
from stock_data_api import FetchStockAPIData
from yahoo_finance_top_stock_gainers import YahooFinanceTopStockGainers
from datetime import date
import config

def extract():
    yahooFinTopStocks = YahooFinanceTopStockGainers().get_top_stocks_gainers()
    df_final = pd.DataFrame()
    for key, value in yahooFinTopStocks.items():
        print(f"Extract Historical Stock Data - {key}, {value}")
        stock_data = FetchStockAPIData(config.API_KEY, key).getStockData()
        df = pd.DataFrame(stock_data)
        df['last_refreshed_date'] = date.today()
        df['stock_symbol'] = key
        df['stock_name'] = value
        df_final = pd.concat([df_final, df])
         
    return df_final

def transform(data):
    print("Transforming Data")
    data['date'] = pd.to_datetime(data['date'])
    data['last_refreshed_date'] = pd.to_datetime(data['last_refreshed_date'])
    return data


def load_to_sqlite(data):
    conn = sqlite3.connect('db/db_stocks')
    print("Writing to DB")
    data.to_sql('stocks', con=conn, if_exists='replace')
    conn.commit()
    conn.close()

def main():
    df = extract()
    df_transformed = transform(df)
    load_to_sqlite(df_transformed)
    
    
if __name__ == "__main__":
    main()
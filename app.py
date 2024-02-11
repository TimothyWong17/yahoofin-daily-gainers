from flask import Flask, render_template, request, url_for
import pandas as pd
from db import DB


def getListofStocksInDataset():
    db_conn = DB('db/db_stocks')
    df = db_conn.get_table_data('stocks')
    stocks = df[['stock_symbol', 'stock_name']].drop_duplicates().values
    last_refresh_date  = df['last_refreshed_date'].iloc[0].split(" ")[0]
  
    return stocks, last_refresh_date

def getLineGraphData(stock_symbol):
    db_conn = DB('db/db_stocks')
    df = db_conn.get_table_data('stocks')
    lineGraphDataByStock = df[df['stock_symbol'] == stock_symbol][['stock_symbol', 'stock_name', 'date', 'open', 'high', 'low', 'close']]
    stock_name = lineGraphDataByStock['stock_name'].iloc[0]
    labels = lineGraphDataByStock['date'].values.tolist()[:20]
    labels = [label.split(" ")[0] for label in labels]
    values = lineGraphDataByStock[['open', 'close', 'high', 'low']].values.tolist()[:20]
    
    return stock_symbol, stock_name, list(reversed(labels)), list(reversed(values))

app = Flask(__name__)

@app.route('/')
def index():
    top_10_daily_gainers, last_refresh_date = getListofStocksInDataset()
    return render_template('index.html', top_10_daily_gainers=top_10_daily_gainers, last_refresh_date=last_refresh_date)


@app.route('/',  methods=['POST'])
def chart():
    top_10_daily_gainers, last_refresh_date = getListofStocksInDataset()
    stock_selected = request.form['stock_select']
    stock_symbol, stock_name, labels, values = getLineGraphData(stock_selected)
    return render_template('index.html',top_10_daily_gainers=top_10_daily_gainers, last_refresh_date=last_refresh_date, labels=labels, values=values, stock_symbol=stock_symbol, stock_name=stock_name)


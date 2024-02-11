import requests

#https://site.financialmodelingprep.com/developer/docs#charts

class FetchStockAPIData:
    def __init__(self, API_KEY, stock_symbol):
        self.stock_price_api_url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{stock_symbol}?apikey={API_KEY}'
        
    def getStockData(self):
        r = requests.get(self.stock_price_api_url)
        data= r.json()
        return data['historical']

        

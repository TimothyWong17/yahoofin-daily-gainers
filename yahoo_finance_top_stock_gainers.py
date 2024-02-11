from bs4 import BeautifulSoup
import requests

class YahooFinanceTopStockGainers:
    def __init__(self):
        self.url = 'https://finance.yahoo.com/gainers/'
        self.top_stocks = {}
        
    def get_top_stocks_gainers(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        stock_tablelists = soup.find_all("table", {"class": "W(100%)"})
        top_stocks = stock_tablelists[0].find_all("a", {"class": "Fw(600)"})
        for i in range(10):
            self.top_stocks[top_stocks[i].text] = top_stocks[i]['title']
        return self.top_stocks
    
            

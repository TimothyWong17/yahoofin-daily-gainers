# yahoofin-daily-gainers
* Front-end
  * Created form to allow users to select top 10 Yahoo Daily Gainer Stocks from SQLite DB
  * Used ChartJS to display line graph of selected stock to show last 20 days of stock price trend
* Back-end
  * Webscrapped data from Yahoo Daily Finance Page to get Top 10 stocks
  * Inputed Scrapped stock data to https://site.financialmodelingprep.com API to get historical stock price data
  * ETL process to transform and format data then store in SQLite DB

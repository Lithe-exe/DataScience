import yfinance as yf
# Download historical data for a stock
appl = yf.Ticker("AAPL")
# get all time market data 
appl_data = appl.history(period="max")
# Display the downloaded data
appl_data.head()
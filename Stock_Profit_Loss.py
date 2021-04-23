import yfinance as yf

#data=[]

data = yf.download(tickers='AAPL',period='1d', interval='1m')

#print(data)

aapl = yf.Ticker("AAPL")

high = aapl.info["dayHigh"]
low = aapl.info["dayLow"]

Maximum = high - low 

#round(Maximum,2)

print(high)
print(low)
print("Maximun Profit for the trading for the day will be: "+ "{:.2f}".format(Maximum,2))
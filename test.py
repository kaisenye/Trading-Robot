import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft)

print(msft.history(period="max"))
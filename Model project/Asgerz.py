## CAPM ## 

import yfinance as yf

msft = yf.Ticker("MSFT")
hist = msft.history(period="5d")
print(hist)

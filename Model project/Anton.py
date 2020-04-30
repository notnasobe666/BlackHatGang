## CAPM ## 

## install pip yfinance

## packages and imports
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import ipywidgets as widgets
import scipy.stats as scs
import scipy.optimize as sco
import statsmodels.api as sm
import scipy.interpolate as sci
from pandas_datareader import data as pdr
import yfinance as yf

# msft = yf.Ticker("msft")
# hist = msft.history(start=start_date, end=end_date)
# print(hist["Close"])

start_date = datetime.datetime(2010,1,1)
end_date = datetime.datetime(2020,1,1)

yf.pdr_override() # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo(["SPY","AAPL"], start=start_date, end=end_date)
data["Adj Close"].head(5)

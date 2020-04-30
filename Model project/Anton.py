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

################################################################

# Time period and stocks: 
start_date = datetime.datetime(2010,1,1)
end_date = datetime.datetime(2020,1,1)
sym = ["AAPL","MSFT","GOOG","AVAV", "RACE"]

# get data as dataframe:
yf.pdr_override() 
data = pdr.get_data_yahoo(sym, start=start_date, end=end_date)["Adj Close"]
data.iloc[np.r_[0:2, -2:0]]

################################################################

# Calculate log daily returns

log_daily_return = np.log(data / data.shift(1))
log_daily_return.head(5)

# log returns to avoid compound effect

###############################################################

# plot log_daily_returns

plt.figure(figsize=(14, 7))
for c in log_daily_return.columns.values:
    plt.plot(log_daily_return.index, log_daily_return[c], lw=3, alpha=0.8, label=c)
plt.legend(loc='upper night', fontsize=12)
plt.ylabel('daily returns')
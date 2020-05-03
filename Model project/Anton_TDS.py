# Streng kopi af tds artikel

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

start_date = datetime.datetime(2010,1,1)
end_date = datetime.datetime(2020,1,1)
sym = ["RICK","PM","AVAV", "RACE","LVS","CGC","TIF","TSLA"]
data = pdr.get_data_yahoo(sym, start=start_date, end=end_date)["Adj Close"]
data.head()





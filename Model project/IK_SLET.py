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

np.random.seed(666)

################################################################

# Expected return = Beta * (Market risk premium)
# Market risk premium = Expected market return - risk free return

# Time period and stocks: 
start_date = datetime.datetime(2010,1,1)
end_date = datetime.datetime(2020,1,1)
sym = ["RICK","PM","AVAV", "RACE","LVS","CGC","TIF","TSLA"]

# get data as dataframe:
yf.pdr_override() 
data = pdr.get_data_yahoo(sym, start=start_date, end=end_date)["Adj Close"]
data.iloc[np.r_[0:2, -2:0]]

risk_free_rate = pdr.get_data_yahoo("^TNX",start='2020-01-01',end='2020-01-01')["Adj Close"]
risk_free_rate

################################################################
# Calculate log daily returns

log_daily_return = np.log(data / data.shift(1))
log_daily_return.iloc[np.r_[0:2, -2:0]]

# log returns to avoid compound effect

################################################################

# stock performance
# evt kombinér stock performance + daily returns 

Performance = log_daily_return.cumsum() * 100
Performance.iloc[np.r_[0:2, -2:0]]


plt.figure(figsize=(14, 7))
for x in log_daily_return.columns.values:
    plt.plot(log_daily_return.index, Performance[x], lw=1, alpha=1, label=x)
plt.legend(fontsize=12)
plt.ylabel('Cumulative return, in %')


################################################################

# plot log_daily_returns

plt.figure(figsize=(14, 7))
for c in log_daily_return.columns.values:
    plt.plot(log_daily_return.index, log_daily_return[c],lw=1, alpha=1, label=c)
plt.legend(fontsize=12)
plt.ylabel('Daily returns')

################################################################

yearly_trading_days = 253

# Mean returns, YoY

AY_return = log_daily_return.mean() * yearly_trading_days
Avg_yearly_return = pd.DataFrame()
Avg_yearly_return["Avg. annual return"] = AY_return 
Avg_yearly_return["Avg. annual return"] = pd.Series(["{0:.2f}%".format(val*100) for val in Avg_yearly_return['Avg. annual return']],index = Avg_yearly_return.index)
Avg_yearly_return

# Covariance Matrix with mean return

CovMatrix = log_daily_return.cov() * yearly_trading_days
CovMatrix

################################################################

# Minimum variance portfolio - only for check, not an algo

# 1) Invert the Cov Matrix

CovMatrix_old = pd.DataFrame(CovMatrix, columns=sym)
Inverted = pd.DataFrame(np.linalg.inv(CovMatrix_old))
Inverted
# 2) indsæt lige vægte (1 taller)
Min_weights = pd.DataFrame([1,1,1,1,1,1,1,1])

# 3) =MMULT()  python version + printer vægte
x = Inverted.dot(Min_weights)
x['Min. var. port weights'] = x / x.sum() * 100
x 

################################################################

# Define return, std. dev & Sharp ratio for portolio - also create random weights

# weights first 
Countticker = len(sym)
weights = np.random.random(Countticker)
weights /= np.sum(weights)
weights
weights.sum()

# then defining portfolio function

def portfolio(weights): 
    weights = np.array(weights)
    Portfolio_return = np.sum(log_daily_return.mean() * weights) * yearly_trading_days 
    Portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(log_daily_return.cov()*yearly_trading_days, weights)))
    return np.array([Portfolio_return,Portfolio_risk, Portfolio_return / Portfolio_risk])

# then a function for the min. variance portfolio can be defined

def min_var_portfolio(weights):
    return -portfolio(weights)[2]



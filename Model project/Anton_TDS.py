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

data.info()

table = data
table.head()

plt.figure(figsize=(14, 7))
for c in table.columns.values: 
    plt.plot(table.index, table[c], lw=1,alpha=0.8,label=c)
plt.legend(fontsize=10)
plt.ylabel('Price in USD')

returns = table.pct_change()
plt.figure(figsize=(14, 7))
for c in returns.columns.values: 
    plt.plot(returns.index, returns[c], lw=1,alpha=0.8,label=c)
plt.legend(fontsize=10)
plt.ylabel('Daily returns')

# calculating annualised return and std dev


def portfolio_annualised_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns*weights ) *252
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    return std, returns

def random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate):
    results = np.zeros((3,num_portfolios))
    weights_record = []
    for i in xrange(num_portfolios):
        weights = np.random.random(4)
        weights /= np.sum(weights)
        weights_record.append(weights)
        portfolio_std_dev, portfolio_return = portfolio_annualised_performance(weights, mean_returns, cov_matrix)
        results[0,i] = portfolio_std_dev
        results[1,i] = portfolio_return
        results[2,i] = (portfolio_return - risk_free_rate) / portfolio_std_dev
    return results, weights_record

returns = table.pct_change()
mean_returns = returns.mean()
cov_matrix = returns.cov()
num_portfolios = 10000
risk_free_rate = 0.00618

def display_simulated_ef_with_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate):
    results, weights = random_portfolios(num_portfolios,mean_returns, cov_matrix, risk_free_rate)
    
    min_vol_idx = np.argmin(results[0])
    sdp_min, rp_min = results[0,min_vol_idx], results[1,min_vol_idx]
    min_vol_allocation = pd.DataFrame(weights[min_vol_idx],index=table.columns,columns=['allocation'])
    min_vol_allocation.allocation = [round(i*100,2)for i in min_vol_allocation.allocation]
    min_vol_allocation = min_vol_allocation.T
    
    print("Minimum Volatility Portfolio Allocation\n")
    print("Annualised Return:", round(rp_min,2))
    print("Annualised Volatility:", round(sdp_min,2))
    print("\n")
    print(min_vol_allocation)

display_simulated_ef_with_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate)



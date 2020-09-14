# -*- coding: utf-8 -*-
"""
@author: io
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as data

tickers = ['TSLA','NFLX', 'HEINY']
start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2020, 8, 30)
assets = pd.DataFrame([data.DataReader(ticker, 'yahoo', start, end)['Adj Close'] for ticker in tickers]).T
assets.columns = tickers
assets = assets/assets.iloc[0, :]

port_rets = assets.pct_change().dropna().mean(axis=1)
port = (assets.pct_change().dropna().mean(axis=1) + 1).cumprod()
assets.plot(alpha=0.4)
port.plot(label='Portfolio', color='black')
plt.legend()
plt.show()

mu = port_rets.mean()
sigma = port_rets.std()
print(f'Portfolio mean return value is {round(mu*100,2)}%')
print(f'Portfolio standard deviation value is {round(sigma*100,2)}%')

port_mc = pd.DataFrame([(np.random.normal(loc=mu, scale=sigma, size=252)+1) for x in range(1000)]).T.cumprod()
port_mc.plot(legend=False, linewidth=1, alpha=0.2, color='green')


port_rets.describe()


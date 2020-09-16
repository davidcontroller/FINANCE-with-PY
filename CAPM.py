# -*- coding: utf-8 -*-
"""
@author: io
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from scipy import stats
import pandas_datareader.data as data

firm = ['NFLX', 'SPX']
start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2017, 1, 1)
assets = pd.DataFrame([data.DataReader(ticker, 'yahoo', start, end)['Adj Close'] for ticker in firm]).T
assets.columns = firm
#CUMULATIVE
assets = assets/assets.iloc[0, :]

assets['NFLX'].plot(label='NETFLIX', color='black')
assets['SPX'].plot(label='SPX', color='red')
plt.legend()
plt.show()

#RET GIORN.
rets = assets.pct_change().dropna()

histo = rets.hist(bins=7)
plt.show()

beta,alpha,r_value,p_value,std_err = stats.linregress(rets['SPX'], rets['NFLX'])




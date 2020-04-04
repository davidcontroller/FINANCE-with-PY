# -*- coding: utf-8 -*-
"""
@author: io

"""

#Breve esempio di grafico utilizzando reali dati finanziari

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import plotly.offline as plyo
import cufflinks as cf
from datetime import datetime
import seaborn as sn
plt.style.use('seaborn') 

data = pd.read_csv(r'C:\Users\...\Dati simulazione\trade_20181127.csv')

data = data[data.symbol == 'XBTUSD']
data['timestamp'] = data.timestamp.map(lambda t: 
    datetime.strptime(t[:-3], “%Y-%m-%dD%H:%M:%S.%f”))

quote = data['grossValue']  
quote = quote.iloc[-1000:]

date = data['timestamp']
date = date.iloc[-1000:]

plt.plot(date,quote)
plt.xlabel('DATA')
plt.ylabel('GROSS VALUE')
plt.title('TEST GRAFICO')
plt.show()

    

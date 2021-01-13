#!/usr/bin/env python
# coding: utf-8

# In[3]:


#get_ipython().run_line_magic('matplotlib', 'inline')

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style 
import mplfinance as mpf
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web


# querying data using pands_dataReader and using yahoo finance api

# In[4]:


style.use('ggplot')
start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 21)

df = web.DataReader('TSLA', 'yahoo',start, end)


# In[ ]:


# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#df.dropna(inplace=True)
df.info()


# In[ ]:


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

# plt.show()


# In[23]:


df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc['volume'] = df['Volume'].resample('10D').sum()


# In[24]:


mpf.plot(df_ohlc, type='candle', volume=True, style='yahoo')


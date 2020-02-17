import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
%matplotlib inline
gld=pdr.get_data_yahoo('GLD','2016-11-08')
gld_close=pd.DataFrame(gld.Close)
gld_close['MA_9']=gld_close.Close.rolling(9).mean()
gld_close['MA_9']=gld_close.Close.rolling(21).mean()
plt.figure(figsize=(15,10))
plt.grid(True)
plt.plot(gld_close['Close'],label='GLD')
plt.plot(gld_close['MA_9'],label='NA 9 DAY')
plt.legend(loc=2)
gld_close['change']=np.log(gld_close['Close']/gld_close['Close'].shift())
gld_close['Volatility']=gld_close.change.rolling(21).std().shift()
gld_close['Volatility'].plot()
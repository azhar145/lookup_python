import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
style.use('ggplot')

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()
df = yf.download("TSLA", start, end)
##print df
print('Ticker',df.tail())
df['Adj Close'].plot()
plt.show()
##df.reset_index(inplace=True)
##df.set_index("Open", inplace=True)
####df = df.drop("Symbol", axis=1)
##
##print(df.tail())
      

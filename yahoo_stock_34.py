# Install yfinance package.
# !pip install yfinance
# Import yfinance
import yfinance as yf  
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('C','2016-01-01','2020-05-21')
# Plot the close prices

g=('TSLA','S','F')
##start = dt.datetime(2017, 7, 1)
##end = dt.datetime.today()
##f=open("u44f.txt","w+")
for i in g:
        data = yf.download(i,'2016-01-01','2020-05-21')
##        df = web.DataReader(i, "google", start, end)
        print(i,data)


import matplotlib.pyplot as plt
data.Close.plot(g[0])
plt.show(g[0])

# ===========================================
#settings to dynamically display all rows
#that are in a dataframe
import pandas as pd
pd.set_option('display.max_rows', None)


#settings for importing built-in datetime
#and external pandas_datareader libraries
import datetime
import pandas_datareader.data as web


#read symbols from file to python list
symbol = []
with open('C:\python_programs\long_stock_symbol_list.txt') as f:
    for line in f:
        symbol.append(line.strip())
f.close


#setting for start and end dates
#notice that the output corresponds to
#a one-year look-back window instead of
#a lookback window for the start and
#end parameter values
start = datetime.datetime(2016, 9, 1)
end = datetime.datetime(2017, 9, 30)



#iterate over ticker symbol values
#while retrieving historical and
#displaying historical stock prices
i=0
while i<len(symbol):
    f = web.DataReader(symbol[i], 'google', start, end)
    f.insert(4,'Symbol',symbol[i])
    print (f)
    i=i+1

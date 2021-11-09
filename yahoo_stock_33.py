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

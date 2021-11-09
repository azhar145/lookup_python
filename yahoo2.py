# Install yfinance package.
# !pip install yfinance
# Import yfinance
import yfinance as yf
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date

yf.pdr_override()
lista=['lk','kos']

f = pdr.get_data_yahoo(lista, '2020-06-01','2020-09-09')
print(f)

new_list = []


for rec in f:
    new_list.append(rec)

print(new_list.head())

##data = yf.download(lista,'2020-06-01','2020-09-09')
### Plot the close prices
##
####data5[]=data[['Close','Open']]
##data['delta_open_close']=data['Close']-data['Open']
##print(data)
###########################3
##import numpy as np
##plt.plot(data.Volume, color="blue", linewidth=1.0, linestyle="-")
##plt.yticks(np.arange(7928200, 124458681, 7928200)) 
####X = np.linspace(-np.pi, np.pi, 256)
####C, S = np.cos(X), np.sin(X)
#############################
##print(data)
####data.Close.plot()
##data.Volume.plot()
##plt.show()

# Install yfinance package.
# !pip install yfinance
# Import yfinance
import yfinance as yf  
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
p=['C','X','F']

for x in p:
    
    data = yf.download(x,'2020-06-05','2020-06-08')
    print(x,'----',data)
# Plot the close prices
##import matplotlib.pyplot as plt
##data.Close.plot()
##plt.show()

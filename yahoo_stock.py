# Install yfinance package.
# !pip install yfinance
# Import yfinance
import yfinance as yf  
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('C','2016-01-01','2020-05-21')
# Plot the close prices
import matplotlib.pyplot as plt
data.Close.plot()
plt.show()

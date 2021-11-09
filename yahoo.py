# Install yfinance package.
# !pip install yfinance
# Import yfinance
import yfinance as yf  
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('lk','2020-05-01','2020-06-20')

# Plot the close prices
import matplotlib.pyplot as plt

###########################3
import numpy as np
plt.plot(data.Volume, color="blue", linewidth=1.0, linestyle="-")
plt.yticks(np.arange(7928200, 124458681, 7928200)) 
##X = np.linspace(-np.pi, np.pi, 256)
##C, S = np.cos(X), np.sin(X)
###########################
print(data)
##data.Close.plot()
data.Volume.plot()
plt.show()

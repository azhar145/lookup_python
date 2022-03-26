import yfinance as yf
import mplfinance as mpf
import yfinance as yf, datetime as dt
import pandas as pd
##    import  datetime as dt
##    today = date.today()
##################################    
##    ticker = "^NDX"
##    no_of_days=200
##    
##    df = pd.DataFrame()
##    start = dt.datetime.today() - dt.timedelta(no_of_days)
##    end = dt.datetime.today()
##    df = yf.download(ticker, start, end)
##    print(df)
####    df.fillna(method='bfill', axis=0, inplace=True)    
##    df['200-day Exponential MA'] = df['Adj Close'].ewm(span=200, adjust=False).mean()
##    df['13-day Exponential MA'] = df['Adj Close'].ewm(span=13, adjust=False).mean()
##    df['50-day Exponential MA'] = df['Adj Close'].ewm(span=50, adjust=False).mean()
##    df['3-day Exponential MA'] = df['Adj Close'].ewm(span=3, adjust=False).mean()
##    print(df)
####    mpf.plot(df, volume=True, tight_layout=True, style="yahoo", type="candle", mav=(3,5,7,13,50),title=ticker+' - ('+perd + ' - '+intervl+')')
##    mpf.plot(df, volume=True, tight_layout=True, style="yahoo", type="candle", mav=(3,5,7,13,50),title=ticker +' (Daily)',show_nontrading=True)
####    df.plot()
################################## Daily ############################
ticker = "tsla"
##ticker=input("Enter stock ticker: ")
no_of_days=180

df = pd.DataFrame()
start = dt.datetime.today() - dt.timedelta(no_of_days)
end = dt.datetime.today()
df = yf.download(ticker, start, end)
df=df[['Open', 'High', 'Low', 'Close']]

df.reset_index(inplace=True)
print(df.columns)


df.columns=['Date','OPEN','HIGH','LOW','CLOSE']
##print(HAdf)
##HAdf = df[['OPEN', 'HIGH', 'LOW', 'CLOSE']]
##HAdf['CLOSE'] = round(((df['OPEN'] + df['HIGH'] + df['LOW'] + df['CLOSE'])/4),2)
##
##for i in HAdf.index:
##    HAdf['OPEN'].loc(i) = HAdf['OPEN'].loc(i) 

##for i in range(len(HAdf)):
##    if i == 0:
##        HAdf.iat[0,0] = round(((df['OPEN'].iloc[0] + df['CLOSE'].iloc[0])/2),2)
##    else:
##        HAdf.iat[i,0] = round(((HAdf.iat[i-1,0] + HAdf.iat[i-1,3])/2),2)


##HAdf['HIGH'] = HAdf.loc[:,['OPEN','CLOSE']].join(df['HIGH']).max(axis=1)
##HAdf['LOW'] = HAdf.loc[:,['OPEN','CLOSE']].join(df['LOW']).min(axis=1)
##
##HAdf.tail(10)
##
import plotly.graph_objects as go


b=df['CLOSE'].max()
b=b+.01*b
m=df['CLOSE'].min()
m=m-.01*m


fig1 = go.Figure(data=[go.Ohlc(x=df.Date,
##fig1 = go.Figure(data=[go.Candlestick(x=HAdf.Date,
                open=df.OPEN,
                high=df.HIGH,
                low=df.LOW,
                close=df.CLOSE
                )])


fig1.update_layout(yaxis_range = [m,b], 
           title = 'Candlestick Chart:' + ticker, 
           xaxis_title = 'Date', 
           yaxis_title = 'Price',
           legend_title_text = "sxhst")
fig1.show()

# https://plotly.com/python/ohlc-charts/

import pandas as pd
import sys,os
import csv
##from pandas import ExcelWriter

m1='stocks_via_proxy_CNN_2u2.txt'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 999999)
pd.set_option('display.width', 2000)

# https://datascience.stackexchange.com/questions/48049/valueerror-could-not-convert-string-to-float
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html
##df1 = pd.read_csv(m1,delimiter=';', error_bad_lines=False)

df1 = pd.read_csv(m1,delimiter='*')

##ticker; Industry;Sector;Corporate Headquater;prev close;Volume;Day’s range;todays close;Today’s open;Average volume (3 months)
##df1.columns = ['ticker'; 'Industry';'Sector';'Corporate Headquater';'prev close';'Volume';'Day’s range';'todays close';'Today’s open';'Average volume (3 months)']
df1.columns = ['tick', 'Industry','Sector','Corporate Headquater','price','Vol','Day’s range','todays close','Today’s open','Average volume (3 months)']
##df1.columns = ['tick', 'exchange', 'comp','price','vol','ff']
##print(df1[['tick', 'Industry','Sector','price','Vol']])
print(df1[['tick','Vol','price','Industry','Sector','Corporate Headquater']])
''
##df1['vol'] = df1['vol'].astype(np.int)
##df1['vol'] = df1.vol.str.replace('\$|\.|\,', '').astype(int)
##print(df1['vol'])
##df1.rename(columns={"index": "num", 'two': "", 'three': 'Price', 'hh': 'Vol'})
##print(df1[['tick','price','vol','comp']])
##print(df1[['tick','price','vol']])
print(df1.dtypes)
# Change data type of column 'Marks' from int64 to float64

df1['price'] = pd.to_numeric(df1['price'], errors='coerce')
df1['vol'] = pd.to_numeric(df1['vol'], errors='coerce')
print(df1.dtypes)
##print(df1)
##p=df1.loc[df1['price'] < 1.0]
p=df1.loc[(df1['price'] < 2.0) &  (df1['vol'] < 60000000) &  (df1['vol'] > 10000000)]
p.reset_index(drop=True)
p.set_index('tick',inplace=True)
##print(p.sort_values(by=['vol','price']))
print(p.sort_values(by=['vol'], ascending=False, na_position='first'))
##print(p[['tick','price','vol','comp','exchange']].count())
'''


import pandas as pd
import ssl

pd.set_option('display.max_rows', 79000)
ssl._create_default_https_context = ssl._create_unverified_context
url = '/home/az2/Downloads/wells_fargo_parse.txt'
df = pd.read_csv(url)
##print(df.shape)
##print(df.describe)
print(df.columns)
##print(df.index)
df.reset_index(drop=True)
##print(df.index)
print(df.dtypes)
##x=['x1','x2','x3','loop','delete']
##df.drop(x,axis=1,inplace=True)
####print(df.head)    
##df.to_csv('/home/az2/Downloads/wells_fargo_parse.txt')
####print (df.shape)
####print (df.columns)
####df.set_index('Account_no',inplace=true)
##print(df['name'].value_counts())
##df.reset_index(drop=True)
##df.set_index('sex',inplace=True)
##print(df.groupby(['State','Store','occupt']).size())
####

##h=['name' ,'sex', 'age', 'Store',
##       'year', 'occupt', 'Accnt_no', 'Balance']
h=['sex', 'age', 'Store',
      'year', 'occupt', 'Accnt_no', 'Balance']

df.drop(h,axis=1,inplace=True)
print(df.columns)
print(df['name'].apply(len).max(),df['Account_no'].apply(len).max(),df['State'].apply(len).max())

##print(df.loc[df[['name']].apply(lambda x: x.str.len().max(), axis=1).idxmax()])

                               
##print(df)
df.iloc[:10500,[1,2,3]].to_csv('/home/az2/Downloads/wells_fargo_parse_8.txt',encoding='utf-8', index = False, header = False,sep = '|')

##print(df.iloc[:5, :])
##df.to_csv('/home/az2/Downloads/wells_fargo_parse_6.txt',index=False, header = False).drop(['unnamed 0'],axis=1)

df2=df1.T
print(df2)

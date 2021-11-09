
import pandas as pd
pd.set_option('display.max_rows', 999999)
pd.set_option('display.max_columns', 99)

g=pd.read_csv('/home/az2/Downloads/Database24.txt',delimiter=';', index_col=None, engine='python')
print(g.head(3))

import os
import pandas as pd

##df = pd.read_fwf('/home/az2/Downloads/test53.txt', header=None,delim_whitespace=True)
df=pd.read_fwf('/home/az2/Downloads/test53.txt', colspecs='infer', widths=None, header=None)



##df = pd.read_csv('/home/az2/Downloads/test53.txt', header=None,delim_whitespace=True)
##df = pd.read_csv('/home/az2/Downloads/test53.txt', skiprows=range(9), header=None, delim_whitespace=True)



print(df.shape)
print(df[5])
##print(df.shape)
print(df[[8,7,6,5]])

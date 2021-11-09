import pandas as pd

g=pd.DataFrame({'name':['ggg','ggg','uuu','ytt'],'sex':['M','F','F','F']})
g.reset_index(drop=True)
##g.set_index('sex',inplace=True)
g.drop_duplicates(keep='first')
t=g.drop([0,1,2])
print(t)
##print (g.loc[(g['name']=='ggg') & (g['sex']=='M')])

import pandas as pd
h=pd.DataFrame({'name':['asad','azhar','naheed','Fatima'],
                'age':[53,51,48,39]})

##print(h[(h['name'] == 'azhar') & (h['age'] == 51)])
##print(h.loc[:,'age'])
h.reset_index(drop=True)
h.set_index('name',inplace=True)

print(h)


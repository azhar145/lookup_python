import pandas as pd

h=pd.DataFrame({'Name':['hh','uu','ff','hh','pp'],
                'Gender':['M','F','M','F','M'],
                'Score':[65,88,86,75,55]})

h.reset_index(drop=True)
##h.set_index('Gender',inplace=True) 
##print(h.Gender.value_counts())
##print(h.Gender.unique())
##print(h.gr(oupby(['Score']).sum())
##print(h.loc[(h['Name']=='hh') & (h['Score'] > 70)])
h.loc[h['Score'] < 80]='jjjjjjjjj'
print(h)

import pandas as pd

h=pd.DataFrame({'name': ['Asad','Azhar','Naheed', 'Fatima','Ammi Jaan'],
                'Age': [53,51,48,40,80],
                'Martial':['M','S','M','S','S']})


##print(h.head())
##h.reset_index(drop=True)
##h.set_index('name',inplace=True)
##print(h.Martial.value_counts())
##print(h.loc[h['name']=='Asad'])
print(h.loc[1,'name'])

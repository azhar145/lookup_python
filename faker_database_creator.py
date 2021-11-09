##import pandas as pd
##pd.set_option('display.max_rows', 999999)
##pd.set_option('display.max_columns', 99)
##pd.set_option('display.width', 2000)
##
##g=pd.read_csv('/home/az2/Downloads/Database23.txt',delimiter=';', index_col=None, engine='python', header=None)
##g.drop(g.index[[0,1]])
##print(g.shape)
##print(g.head(3))
##a=["dd","ff","aad"]
##g.columns=["name","job","comp","trash"]

##print(g.shape)
##g['bb']=len(g.name.str.lstrip())
##print(g)
##g.to_csv('/home/az2/Downloads/Database24.txt',index=False, sep=';' , header=True)
##print(g.head(3))
##print(g.head(3))
##print(g.columns)
##print(g.head(4))
##print(g['dd'].apply(len).max())
##      '   ',
##      g['job'].apply(len).max())
##import pandas as pd
##pd.set_option('display.max_columns', None)

##
##g=pd.read_csv('/home/az2/Downloads/Database22.txt', encoding='ISO-8859-1', engine='python', header=None)
##print(g.shape)
##g=pd.read_csv('/home/az2/Downloads/Database22.txt', delimiter=';',encoding='ISO-8859-1', engine='python', header=None)
##print(g.shape)
##
##a=['name','Address','DOB', 'JOB','Company','SSN']
##g.columns=a
##print(g.shape)
##
####print(g.head(4))
##
##print(g['name'].apply(len).max(),
##      g['Address'].apply(len).max(),
##      g['DOB'].apply(len).max(),
##      g['JOB'].apply(len).max(),
##      g['Company'].apply(len).max(),
##      g['SSN'].apply(len).max()
##      )

#########################################
##Step 1:
##
##CREATE TABLE qq
##        (
##        name varchar(16),
##	Address varchar(43),
##        DOB varchar(10),
##        JOB varchar(29),
##        Company varchar(25),
##        SSN varchar(11)
##        )
#######################################                    );
##Step2: (in ubuntu terminal or unix terminal  with vi)
##n9.ctl: (create with vi n.ctl)
##
##LOAD DATA
##INFILE  '/home/az2/Downloads/Database22.txt'
##BADFILE '/home/az2/Downloads/Database22.bad'
##DISCARDFILE '/home/az2/Downloads/Database22.dsc'
##INSERT INTO TABLE qq
##FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' TRAILING NULLCOLS
##(name,Address,DOB, JOB,Company,SSN);
###########################################        
##Step3:
##    sqlldr userid=system/1 control=/home/az2/Downloads/n9.ctl log=n9.log 

#########################################
from faker import Faker
import pandas as pd
fake = Faker('en_US')
##x='/home/az2/Downloads/Database24.txt'
f=open( '/home/az2/Downloads/Database24.txt' , 'w+', encoding='ISO-8859-1')
f.write("x1")
f.write(";")
f.write("x2")
f.write(";")
f.write("x3")
f.write(";")
f.write("x4")
f.write('\n')
for x in range(1000000):
    f.write('"')
    f.write(fake.name_male())
    f.write('"')
    f.write(';')
    f.write('"')
    f.write(fake.name_female())
    f.write('"')
    f.write(';')
    f.write('"')
    f.write(fake.job())
    f.write('"')
    f.write(';')
    f.write('"')
    f.write(fake.ssn())
    f.write('"')
    f.write('\n')
f.close()

g=pd.read_csv('/home/az2/Downloads/Database24.txt',delimiter=';', index_col=None, engine='python')
print(g.shape)
print('x1','  ', g["x1"].apply(len).max())
print('x2','  ', g["x2"].apply(len).max())
print('x3','  ', g["x3"].apply(len).max())
print('x4','  ', g["x4"].apply(len).max())
##g=g.to_csv('/home/az2/Downloads/Database24a.txt')

# remove header row
import pandas as pd
pd.set_option('display.max_rows', 999999)
pd.set_option('display.max_columns', 99)
pd.set_option('display.width', 2000)

##g=pd.read_csv('/home/az2/Downloads/Database24a.txt',delimiter=';', index_col=None, engine='python', header=None)
##print(g.shape)
##print(g.columns)
##g=g.drop(index=0)
####pd.to_csv('/home/az2/Downloads/Database24.txt',index_col=None, header=None)
####g.to_csv('/home/az2/Downloads/Database24.txt',index=False, sep=';' , header=None)
##g.to_csv('/home/az2/Downloads/Database24.txt',index=False, header=None)
##print(g.head(2))
##g.iloc[:10,[0,1,2]].to_csv('/home/az2/Downloads/Database24a.txt',encoding='utf-8', index = False, header = False,sep = ';')
##g.iloc[:,[0,1,2]].to_csv('/home/az2/Downloads/Database24a.txt',encoding='utf-8', index = False, header = False,sep = ';')
##print('\n\n\n\n')
##g.to_csv('/home/az2/Downloads/Database24.txt',index=False, sep=';' , header=None)
##g=pd.read_csv('/home/az2/Downloads/Database24a.txt',delimiter=';', index_col=None, engine='python', header=None)
##g=g.drop(index=0)
##print(g1.head(2))

####    f.write(fake.building_number()+' '+fake.street_name() +', '+ fake.city() +', ' +fake.zipcode())
####    f.write(';')
####    f.write(str(fake.date_of_birth()))
####    f.write(';')
##    f.write(fake.job())
##    f.write('"')
##    f.write(';')
##    f.write(fake.company())
##    f.write('"')
##    f.write(fake.job())
##    f.write('"')
##    f.write(';')
##
##    f.write('"')
##    f.write(fake.company())
##    f.write('"')
##    f.write(';')
####    f.write(';')
##    f.write('"')
####    f.write(';')
##    f.write(fake.ssn())
##    f.write(';')
####
##    f.write('\n')
##    f.write('\n')
##f.close()


################################################################################3
##
##import pandas as pd
##import ssl
##
##pd.set_option('display.max_rows', 79000)
##ssl._create_default_https_context = ssl._create_unverified_context
##url = '/home/az2/Downloads/wells_fargo_parse.txt'
##df = pd.read_csv(url)
####print(df.shape)
####print(df.describe)
##print(df.columns)
####print(df.index)
##df.reset_index(drop=True)
####print(df.index)
##print(df.dtypes)
####x=['x1','x2','x3','loop','delete']
####df.drop(x,axis=1,inplace=True)
######print(df.head)    
####df.to_csv('/home/az2/Downloads/wells_fargo_parse.txt')
######print (df.shape)
######print (df.columns)
######df.set_index('Account_no',inplace=true)
####print(df['name'].value_counts())
####df.reset_index(drop=True)
####df.set_index('sex',inplace=True)
####print(df.groupby(['State','Store','occupt']).size())
######
##
####h=['name' ,'sex', 'age', 'Store',
####       'year', 'occupt', 'Accnt_no', 'Balance']
##h=['sex', 'age', 'Store',
##      'year', 'occupt', 'Accnt_no', 'Balance']
##
##df.drop(h,axis=1,inplace=True)
##print(df.columns)
##print(df['name'].apply(len).max(),df['Account_no'].apply(len).max(),df['State'].apply(len).max())
##
####print(df.loc[df[['name']].apply(lambda x: x.str.len().max(), axis=1).idxmax()])
##
##                               
####print(df)
##df.iloc[:10500,[1,2,3]].to_csv('/home/az2/Downloads/wells_fargo_parse_8.txt',encoding='utf-8', index = False, header = False,sep = '|')
##
####print(df.iloc[:5, :])
####df.to_csv('/home/az2/Downloads/wells_fargo_parse_6.txt',index=False, header = False).drop(['unnamed 0'],axis=1)
##
##df2=df1.T
##print(df2)


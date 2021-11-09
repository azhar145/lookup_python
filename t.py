def multiple_file_generator(mm):
    import numpy as np
    import pandas as pd

    import random
    import random
    from datetime import datetime, timedelta

    hl7(mm)

'''
    ################### no of rows ##############
    x=200

    items = ['1/2/2020','1/3/2020', '1/4/2020', '1/5/2020', '1/6/2020']
    aa=random.choices(items,k=x)

    n = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Minor Outlying Islands', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'U.S. Virgin Islands', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    t1=np.random.choice(a=n, size=x)

    m=['over_50','over_60','under_50']
    t2=np.random.choice(a=m, size=x)

    ############ Corona virus cases ###################
    g=random.sample(range(0, 300), x)


    d={'Dated': aa,'State':t1,'Status':t2, 'cases':g}
    ##d={'Date':random_date,'State':t1,'Status':t2, 'cases':m}


    df=pd.DataFrame(d)
    df.to_csv("/home/az2/Downloads/t1/" + "BB" + str(mm) + "_"  + ".csv")
##    df.to_csv("/home/az2/Downloads/python_66/b/t1/" + "BB" + str(num_of_files_to_gen_count) + "_" + str(m) + ".csv")
##    print(df)



##print(arr.count)

'''


def no_of_files():
    import os
    file_path = '/home/az2/Downloads/t1/'
    arr = os.listdir(file_path)
    
    k=0
    for p in arr:
        k=k+1
    ##    print(file_path + p)
    ##    os.remove(file_path + '/' + p + '.csv')
    ##    print(p)
    print('now ',k, ' files created')


def delete_files():
    import os
    file_path = '/home/az2/Downloads/t1/'
    arr = os.listdir(file_path)
    
    k=0
    for p in arr:
        k=k+1
    ##    print(file_path + p)
        os.remove(file_path + p)
    ##    print(p)
    print('deleted ',k, ' files')



############################################################
def main ():

 
    m=0
    num_of_files_to_gen_count=int(input("enter no of files: "))+0
    print('no of files ', num_of_files_to_gen_count,' will be created')
    for m in range(num_of_files_to_gen_count):
                  multiple_file_generator(m)
##                  print(m)
                  m=m+1

#####################################################################

def hl7(m):
        from faker import Faker
        import datetime
        import random
        from random import randint
        x = Faker('en_US')
   

        g=open("/home/az2/Downloads/t1/" + "Patient_" + str(m) + "_"  + ".csv", 'w+')
        g.write('MSH|^~\&|ADT1|MCM|LABADT|MCM|198808181126|SECURITY|ADT^A04|MSG00001|P|2.4\n')
        g.write('EVN|A01-|198808181123\n')

        g.write('PID|||')
        g.write('PATID')
        g.write('7659')
        g.write(str(m))
        g.write('||')
        g.write(x.name_male())
         
        g.write('||')
        sd = x.date_between(start_date="-70y", end_date="now")
        delta = datetime.timedelta(days=365*randint(18,90))
        bd = sd-delta
        g.write(str(bd))
        g.write('|M-||2106-3|')
        g.write(x.address())
        g.write('|GL|')
        g.write(x.phone_number())
        g.write('|')
        g.write(x.phone_number())
        g.write('||S||PATID12345001^2^M10|123456789|9-87654^NC|')
        g.write(x.ssn())

        g.close()


      

        
##        print('MSH|^~\&|ADT1|MCM|LABADT|MCM|198808181126|SECURITY|ADT^A04|MSG00001|P|2.4\n')
##        print('EVN|A01-|198808181123\n')
##        print('PID|||PATID1234^5^M11||JONES^WILLIAM^A^III||19610615|M-||2106-3|1200 N ELM STREET^^GREENSBORO^NC^27401-1020|GL|(919)379-1212|(919)271-3434~(919)277-3114||S||PATID12345001^2^M10|123456789|9-87654^NC')
##        print('NK1|1|JONES^BARBARA^K|SPO|||||20011105\n')
##        print('NK1|1|JONES^MICHAEL^A|FTH\n')
##        print('PV1|1|I|2000^2012^01||||004777^LEBAUER^SIDNEY^J.|||SUR||-||1|A0-\n')
##        print('AL1|1||^PENICILLIN||PRODUCES HIVES~RASH\n')
##        print('AL1|2||^CAT DANDER\n')
##        print('DG1|001|I9|1550|MAL NEO LIVER, PRIMARY|19880501103005|F||\n')
##        print('PR1|2234|M11|111^CODE151|COMMON PROCEDURES|198809081123\n')
##        print('ROL|45^RECORDER^ROLE MASTER LIST|AD|CP|KATE^SMITH^ELLEN|199505011201\n')
##        print('GT1|1122|1519|BILL^GATES^A\n')
##        print('IN1|001|A357|1234|BCMD|||||132987\n')
##        print('IN2|ID1551001|SSN12345678\n')
##        print('ROL|45^RECORDER^ROLE MASTER LIST|AD|CP|KATE^ELLEN|199505011201\n')






'''
MSH|^~\&|ADT1|MCM|LABADT|MCM|198808181126|SECURITY|ADT^A04|MSG00001|P|2.4
EVN|A01-|198808181123
PID|||PATID1234^5^M11||JONES^WILLIAM^A^III||19610615|M-||2106-3|1200 N ELM STREET^^GREENSBORO^NC^27401-1020|GL|(919)379-1212|(919)271-3434~(919)277-3114||S||PATID12345001^2^M10|123456789|9-87654^NC
NK1|1|JONES^BARBARA^K|SPO|||||20011105
NK1|1|JONES^MICHAEL^A|FTH
PV1|1|I|2000^2012^01||||004777^LEBAUER^SIDNEY^J.|||SUR||-||1|A0-
AL1|1||^PENICILLIN||PRODUCES HIVES~RASH
AL1|2||^CAT DANDER
DG1|001|I9|1550|MAL NEO LIVER, PRIMARY|19880501103005|F||
PR1|2234|M11|111^CODE151|COMMON PROCEDURES|198809081123
ROL|45^RECORDER^ROLE MASTER LIST|AD|CP|KATE^SMITH^ELLEN|199505011201
GT1|1122|1519|BILL^GATES^A
IN1|001|A357|1234|BCMD|||||132987
IN2|ID1551001|SSN12345678
ROL|45^RECORDER^ROLE MASTER LIST|AD|CP|KATE^ELLEN|199505011201
'''
                  
import time
start_time = time.time()

delete_files()
main()
no_of_files()
gt=int(time.time() - start_time)
if gt > 60:
    gt1=gt/60
    print ("***** Completed  ***** My program took", gt , " mins to run")
else:
    print ("***** Completed  ***** My program took", gt , " secs to run")
    
#####################################################################




def multiple_file_generator(mm):
    import numpy as np
    import pandas as pd

    import random
    import random
    from datetime import datetime, timedelta



    
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
    df.to_csv("/home/az2/Downloads/python_66/b/t1/" + "BB" + str(mm) + "_"  + ".csv")
##    df.to_csv("/home/az2/Downloads/python_66/b/t1/" + "BB" + str(num_of_files_to_gen_count) + "_" + str(m) + ".csv")
    print(df)

m=0
num_of_files_to_gen_count=600
for m in range(num_of_files_to_gen_count):
              multiple_file_generator(m)
              print(m)
              m=m+1
              
    

def m(p):
    import numpy as np
    
    p1=np.log(p)
    p2=p+1
    p3="jjjj"
    return p1,p2,p3


p=6
print("input  ",m(p))
print ("output  ",m(p)[0],m(p)[1],m(p)[2])
x=m(p)[0]
print('x= ',x)

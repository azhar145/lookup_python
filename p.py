from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml
import re
import requests
from itertools import cycle
import traceback2 as traceback
import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
k=0
hy='tumko34'

def s1(url,f):

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import lxml
    import re
    import requests
    from itertools import cycle
    import traceback2 as traceback
    import random
    global k
    htmla = urlopen(url)
    html=htmla.readlines()

    
##    k=0
    k1=0
####################################################################    
    for x in html:        
##        u='<a href="/stockquote/NASDAQ/'
        u='<a href="/stockquote/NYSE/'
##        u='<a href="/stockquote/AMEX/'
        if str(u) in str(x):
            k=k+1
            k1=k1+1
##            NASDAQ
##            print(k,')' ,'   ',str(x[58:70]).split('.')[0])
##            f.write(str(x[58:70]).split('.')[0])
##            NYSE
            print(k,')' ,'   ',str(x[56:76]).split('.')[0],' NYSE')
            f.write(str(x[56:76]).split('.')[0])
##           AMEX
##            print(k,')' ,'   ',str(x[56:78]).split('.')[0])
##            f.write(str(x[56:78]).split('.')[0])
            
            f.write(';')
            f.write(' NYSE')
            if k1==15:
                f.write('\n')
                k1=0
####################################################################
##        u='<a href="/stockquote/NYSE/'
        u='<a href="/stockquote/AMEX/'
        if str(u) in str(x):
            k=k+1
            k1=k1+1
##            NASDAQ
##            print(k,')' ,'   ',str(x[58:70]).split('.')[0])
##            f.write(str(x[58:70]).split('.')[0])
##            NYSE
##            print(k,')' ,'   ',str(x[56:76]).split('.')[0])
##            f.write(str(x[56:76]).split('.')[0])
##           AMEX
            print(k,')' ,'   ',str(x[56:78]).split('.')[0], ' AMEX')
            f.write(str(x[56:78]).split('.')[0])
            
##            f.write(',')
            f.write(';')
            f.write(' AMEX')

            if k1==15:
                f.write('\n')
                k1=0
###############################################################################
##                        u='<a href="/stockquote/NYSE/'
        u='<a href="/stockquote/NASDAQ/'                        
##        u='<a href="/stockquote/AMEX/'
        if str(u) in str(x):
            k=k+1
            k1=k1+1
##            NASDAQ
            print(k,')' ,'   ',str(x[58:70]).split('.')[0],' NASDAQ ', str(x[1:9000]).split(" ")[5] )
            f.write(str(x[58:70]).split('.')[0])
##            NYSE
##            print(k,')' ,'   ',str(x[56:76]).split('.')[0])
##            f.write(str(x[56:76]).split('.')[0])
##           AMEX
##            print(k,')' ,'   ',str(x[56:78]).split('.')[0])
##            f.write(str(x[56:78]).split('.')[0])
            
##            f.write(',')
            f.write(';')
            f.write(' NASDAQ')

            if k1==15:
                f.write('\n')
                k1=0
##############################################################

##            print('\n')
## NASDAQ
##t=['http://eoddata.com/stocklist/NASDAQ/A.htm','http://eoddata.com/stocklist/NASDAQ/B.htm',
##   'http://eoddata.com/stocklist/NASDAQ/C.htm','http://eoddata.com/stocklist/NASDAQ/D.htm',
##   'http://eoddata.com/stocklist/NASDAQ/E.htm','http://eoddata.com/stocklist/NASDAQ/F.htm',
##   'http://eoddata.com/stocklist/NASDAQ/G.htm','http://eoddata.com/stocklist/NASDAQ/H.htm',
##   'http://eoddata.com/stocklist/NASDAQ/I.htm','http://eoddata.com/stocklist/NASDAQ/J.htm',
##   'http://eoddata.com/stocklist/NASDAQ/K.htm','http://eoddata.com/stocklist/NASDAQ/L.htm',
##   'http://eoddata.com/stocklist/NASDAQ/M.htm','http://eoddata.com/stocklist/NASDAQ/N.htm',
##   'http://eoddata.com/stocklist/NASDAQ/O.htm','http://eoddata.com/stocklist/NASDAQ/P.htm',
##   'http://eoddata.com/stocklist/NASDAQ/Q.htm','http://eoddata.com/stocklist/NASDAQ/R.htm',
##   'http://eoddata.com/stocklist/NASDAQ/T.htm','http://eoddata.com/stocklist/NASDAQ/U.htm',
##   'http://eoddata.com/stocklist/NASDAQ/V.htm','http://eoddata.com/stocklist/NASDAQ/W.htm',
##   'http://eoddata.com/stocklist/NASDAQ/X.htm','http://eoddata.com/stocklist/NASDAQ/Y.htm',
##   'http://eoddata.com/stocklist/NASDAQ/Z.htm'
##   ]

## NYSE
##t=['http://eoddata.com/stocklist/NYSE/A.htm','http://eoddata.com/stocklist/NYSE/B.htm'
##   'http://eoddata.com/stocklist/NYSE/C.htm','http://eoddata.com/stocklist/NYSE/D.htm',
##   'http://eoddata.com/stocklist/NYSE/E.htm','http://eoddata.com/stocklist/NYSE/F.htm',
##   'http://eoddata.com/stocklist/NYSE/G.htm','http://eoddata.com/stocklist/NYSE/H.htm',
##   'http://eoddata.com/stocklist/NYSE/I.htm','http://eoddata.com/stocklist/NYSE/J.htm',
##   'http://eoddata.com/stocklist/NYSE/K.htm','http://eoddata.com/stocklist/NYSE/L.htm',
##   'http://eoddata.com/stocklist/NYSE/M.htm','http://eoddata.com/stocklist/NYSE/N.htm',
##   'http://eoddata.com/stocklist/NYSE/O.htm','http://eoddata.com/stocklist/NYSE/P.htm',
##   'http://eoddata.com/stocklist/NYSE/Q.htm','http://eoddata.com/stocklist/NYSE/R.htm',
##   'http://eoddata.com/stocklist/NYSE/T.htm','http://eoddata.com/stocklist/NYSE/U.htm',
##   'http://eoddata.com/stocklist/NYSE/V.htm','http://eoddata.com/stocklist/NYSE/W.htm',
##   'http://eoddata.com/stocklist/NYSE/X.htm','http://eoddata.com/stocklist/NYSE/Y.htm',
##   'http://eoddata.com/stocklist/NYSE/Z.htm'
##   ]

## AMEX
##t=['http://eoddata.com/stocklist/AMEX/A.htm',
##   'http://eoddata.com/stocklist/AMEX/B.htm',
##   'http://eoddata.com/stocklist/AMEX/C.htm','http://eoddata.com/stocklist/AMEX/D.htm',
##   'http://eoddata.com/stocklist/AMEX/E.htm','http://eoddata.com/stocklist/AMEX/F.htm',
##   'http://eoddata.com/stocklist/AMEX/G.htm','http://eoddata.com/stocklist/AMEX/H.htm',
##   'http://eoddata.com/stocklist/AMEX/I.htm','http://eoddata.com/stocklist/AMEX/J.htm',
##   'http://eoddata.com/stocklist/AMEX/K.htm','http://eoddata.com/stocklist/AMEX/L.htm',
##   'http://eoddata.com/stocklist/AMEX/M.htm','http://eoddata.com/stocklist/AMEX/N.htm',
##   'http://eoddata.com/stocklist/AMEX/O.htm','http://eoddata.com/stocklist/AMEX/P.htm',
##   'http://eoddata.com/stocklist/AMEX/Q.htm','http://eoddata.com/stocklist/AMEX/R.htm',
##   'http://eoddata.com/stocklist/AMEX/T.htm','http://eoddata.com/stocklist/AMEX/U.htm',
##   'http://eoddata.com/stocklist/AMEX/V.htm','http://eoddata.com/stocklist/AMEX/W.htm',
##   'http://eoddata.com/stocklist/AMEX/X.htm','http://eoddata.com/stocklist/AMEX/Y.htm',
##   'http://eoddata.com/stocklist/AMEX/Z.htm'
##   ]

## NASDAQ
t=['http://eoddata.com/stocklist/NASDAQ/A.htm','http://eoddata.com/stocklist/NASDAQ/B.htm',
   'http://eoddata.com/stocklist/NASDAQ/C.htm','http://eoddata.com/stocklist/NASDAQ/D.htm',
   'http://eoddata.com/stocklist/NASDAQ/E.htm','http://eoddata.com/stocklist/NASDAQ/F.htm',
   'http://eoddata.com/stocklist/NASDAQ/G.htm','http://eoddata.com/stocklist/NASDAQ/H.htm',
   'http://eoddata.com/stocklist/NASDAQ/I.htm','http://eoddata.com/stocklist/NASDAQ/J.htm',
   'http://eoddata.com/stocklist/NASDAQ/K.htm','http://eoddata.com/stocklist/NASDAQ/L.htm',
   'http://eoddata.com/stocklist/NASDAQ/M.htm','http://eoddata.com/stocklist/NASDAQ/N.htm',
   'http://eoddata.com/stocklist/NASDAQ/O.htm','http://eoddata.com/stocklist/NASDAQ/P.htm',
   'http://eoddata.com/stocklist/NASDAQ/Q.htm','http://eoddata.com/stocklist/NASDAQ/R.htm',
   'http://eoddata.com/stocklist/NASDAQ/T.htm','http://eoddata.com/stocklist/NASDAQ/U.htm',
   'http://eoddata.com/stocklist/NASDAQ/V.htm','http://eoddata.com/stocklist/NASDAQ/W.htm',
   'http://eoddata.com/stocklist/NASDAQ/X.htm','http://eoddata.com/stocklist/NASDAQ/Y.htm',
   'http://eoddata.com/stocklist/NASDAQ/Z.htm',
   'http://eoddata.com/stocklist/NYSE/A.htm','http://eoddata.com/stocklist/NYSE/B.htm'
   'http://eoddata.com/stocklist/NYSE/C.htm','http://eoddata.com/stocklist/NYSE/D.htm',
   'http://eoddata.com/stocklist/NYSE/E.htm','http://eoddata.com/stocklist/NYSE/F.htm',
   'http://eoddata.com/stocklist/NYSE/G.htm','http://eoddata.com/stocklist/NYSE/H.htm',
   'http://eoddata.com/stocklist/NYSE/I.htm','http://eoddata.com/stocklist/NYSE/J.htm',
   'http://eoddata.com/stocklist/NYSE/K.htm','http://eoddata.com/stocklist/NYSE/L.htm',
   'http://eoddata.com/stocklist/NYSE/M.htm','http://eoddata.com/stocklist/NYSE/N.htm',
   'http://eoddata.com/stocklist/NYSE/O.htm','http://eoddata.com/stocklist/NYSE/P.htm',
   'http://eoddata.com/stocklist/NYSE/Q.htm','http://eoddata.com/stocklist/NYSE/R.htm',
   'http://eoddata.com/stocklist/NYSE/T.htm','http://eoddata.com/stocklist/NYSE/U.htm',
   'http://eoddata.com/stocklist/NYSE/V.htm','http://eoddata.com/stocklist/NYSE/W.htm',
   'http://eoddata.com/stocklist/NYSE/X.htm','http://eoddata.com/stocklist/NYSE/Y.htm',
   'http://eoddata.com/stocklist/NYSE/Z.htm',
   'http://eoddata.com/stocklist/AMEX/A.htm',
   'http://eoddata.com/stocklist/AMEX/B.htm',
   'http://eoddata.com/stocklist/AMEX/C.htm','http://eoddata.com/stocklist/AMEX/D.htm',
   'http://eoddata.com/stocklist/AMEX/E.htm','http://eoddata.com/stocklist/AMEX/F.htm',
   'http://eoddata.com/stocklist/AMEX/G.htm','http://eoddata.com/stocklist/AMEX/H.htm',
   'http://eoddata.com/stocklist/AMEX/I.htm','http://eoddata.com/stocklist/AMEX/J.htm',
   'http://eoddata.com/stocklist/AMEX/K.htm','http://eoddata.com/stocklist/AMEX/L.htm',
   'http://eoddata.com/stocklist/AMEX/M.htm','http://eoddata.com/stocklist/AMEX/N.htm',
   'http://eoddata.com/stocklist/AMEX/O.htm','http://eoddata.com/stocklist/AMEX/P.htm',
   'http://eoddata.com/stocklist/AMEX/Q.htm','http://eoddata.com/stocklist/AMEX/R.htm',
   'http://eoddata.com/stocklist/AMEX/T.htm','http://eoddata.com/stocklist/AMEX/U.htm',
   'http://eoddata.com/stocklist/AMEX/V.htm','http://eoddata.com/stocklist/AMEX/W.htm',
   'http://eoddata.com/stocklist/AMEX/X.htm','http://eoddata.com/stocklist/AMEX/Y.htm',
   'http://eoddata.com/stocklist/AMEX/Z.htm'
   ]


# f= open("/home/az2/Documents/" + hy + ".txt","w+")

for x in t:
      
    s1(x,f)
    print('')
# f.close()    






    


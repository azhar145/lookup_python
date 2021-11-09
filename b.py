
def s1(x,gg,startTime):

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import lxml
    # import re
    import random
    import requests
    import random
### proxy ##################################################################################
    proxy1={"http": "http://51.254.237.77:3129"}
    proxy2={"http": "http://176.196.84.138:51336"}
    proxy3={"http":  "http://54.169.9.36:3128"}
    proxy4={"http":  "http://51.158.78.179:8811"}

    dd=[proxy1,proxy2,proxy3,proxy4]
    url = "https://money.cnn.com/quote/quote.html?symb=" + x +"&iid=business_hp_markets"

    proxies=random.choice(dd)
    r = requests.get(url, proxies )
    print(k,')  ',x,'   ', r.status_code,'  def s1(x,gg)--> ',r,'  ggggg ',proxies,'    ',url)
    if r.status_code == 200:
        print("code")


             


t=['F','X','S']



gg='stocks_via_proxy_CNN_nn'

k=0

print("NO of stoks: ",len(t))
print("Will take approx :", 2.4*10, "***** for ", len(t), "will take ",2.4*len(t)/3600, " mins to complete")

##ta=len(t)
fo=open('/home/hadoop/' + gg + '.txt','w')


fo.write('ticker')
fo.write('*')
fo.write('Average volume (3 months)')
fo.write('\n')

from datetime import datetime
startTime = datetime.now()
for x in t:
    k=k+1
##    print('\n')
##    print('\n')ttt
##    print('*********************************************************************************************************\n')
##

    if  k < len(t)+1:
        s1(x,gg,startTime)
        print(k)
    elif k == len(t)+1:
        print("100 complete") 
##    else:
##        break
    
print("end")
fo.close()

print("original time took: ", datetime.now() - startTime,"  Predicted time: ", 2.4*len(t))



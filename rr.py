##def a():
##
##    print('A')
##    p=open('/home/aa/Documents/x.txt','r')
##    g=p.readlines()
##    p=re.findall(r"([a-zA-Z]+) (\d+)",str(g))
##    p=p.group()
####    u=p.start()
##
##    print(p)
##    print('\n')
##    print('\n')
####    for x in g:
######        m=(x.split())
######        print(x)
##

import re
# Lets use a regular expression to match a few date strings.
regex = r"([a-zA-Z]+) (\d+)"
k="A regular expression -y 7766666 is a special sequence of -g 89"
matches = re.finditer(regex, k)
for match in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
     print(k[match.start():match.end()])


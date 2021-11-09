import re

u="A group of Senate Sen5te grcup Democrats unveiled a proposal on Friday"
p= 'Sen(.)te'
for x in u.split():
    pa=re.findall(p,x)
    if len(pa) > 0:
        print(x)

##import re
##s1 = "Mayer is a very common Name"
##s2 = "He is called Meyer but he isn't German."
##print(re.search(r"M[ae][iy]er", s1))

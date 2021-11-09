v=open("/home/az2/Downloads/tr2.txt")
##g=v.read()
##print(g)
for x in v:
    for t in x.split():
        if t in "Python":
            print(t)

v.close()

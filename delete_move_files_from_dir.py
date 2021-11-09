import os
file_path = '/home/az2/Downloads/t1/'
arr = os.listdir(file_path)
##print(arr.count)

k=0
for p in arr:
    k=k+1
##    print(file_path + p)
##    os.remove(file_path + '/' + p + '.csv')
##    print(p)
print(k, 'files')


k=0
for p in arr:
    k=k+1
##    print(file_path + p)
    os.remove(file_path + p)
##    print(p)
print(k, 'files')

path = 'data/'
out=''
for i in range(254):
    out+=open(path+str(i),'r').read()
print out
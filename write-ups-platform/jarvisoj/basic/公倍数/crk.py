flag = 0
for i in xrange(3,1000000000,3):
    flag += i
for i in xrange(5,1000000000,5):
    flag += i
for i in xrange(15,1000000000,15):
    flag -= i
print flag
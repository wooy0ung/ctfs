src="adminadmin1231233"
pad=[7,8,12,14,21,13,13,3,28,22,110,93,64,110,93,88,78]

flag=""
for i in range(17):
  flag+=chr(ord(src[i])^pad[i])

print flag
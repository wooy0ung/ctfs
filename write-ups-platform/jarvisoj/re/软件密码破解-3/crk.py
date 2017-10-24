print "[x0-x3]: "
for x0 in range(256):
	for x1 in range(256):
		if (x0 - x1)%256 == 68:
			for x2 in range(256):
				if (x1 - x2)%256 == 2:
					for x3 in range(256):
						if x2 - x3 == -59 and (x0 + x1 + x2 + x3)%256 == 71:
							print hex(x0),
							print hex(x1),
							print hex(x2),
							print hex(x3)
print "[x4-x7]: "
for x4 in range(256):
	for x5 in range(256):
		if (x4 - x5)%256 == 52:
			for x6 in range(256):
				if (-x4 + x6)%256 == 10:
					for x7 in range(256):
						if (x6 - x7)%256 == 9 and (x5 + x6 + x7)%256 == 3:
							print hex(x4),
							print hex(x5),
							print hex(x6),
							print hex(x7)
							


'''
key[0] + key[1] + key[2] + key[3] == 71
key[5] + key[6] + key[7] == 3
key[0] - key[1] == 68 
key[1] - key[2] == 2
key[2] - key[3] == -59
-key[4] + key[6] == 10
key[6] - key[7] == 9
key[4] - key[5]== 52
'''
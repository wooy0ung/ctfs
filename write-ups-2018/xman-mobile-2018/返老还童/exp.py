#!/usr/bin/python
# -*- coding:utf8 -*-

table = ['0','1','2','3','4','5','6','7','8','9',
		'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
		'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

pad = [0,0,0,0,0,0,0,0]

for i in table:
	if ord(i) % 2 != 1:
		pad[6] = i
		if chr(ord(i) - 8) in table:
			pad[2] = chr(ord(i) - 8)
			if chr(ord(i) | 1) in table:
				pad[3] = chr(ord(i) | 1)
				if chr((ord(i) - 16)/2) in table:
					pad[1] = chr((ord(i) - 16)/2)
					if chr(ord(i) - 8) in table and ((ord(i) - 8) ^ 55) < 100:
						pad[7] = chr(ord(i) - 8)
						if chr((ord(i) | 1) ^ 18) in table:
							pad[5] = chr((ord(i) | 1) ^ 18)
							if chr(((ord(i) | 1) ^ 18) - 3) in table:
								pad[0] = chr(((ord(i) | 1) ^ 18) - 3)
								if chr(((ord(i) | 1) ^ 18) - 5) in table:
									pad[4] = chr(((ord(i) | 1) ^ 18) - 5)
									print pad,ord(pad[7]) ^ 55
print ""
print ""

pad2 = [0,0,0,0,0,0,0,0]

for i in table:
	pad2[1] = i
	if chr(ord(i) + 12) in table:
		pad2[3] = chr(ord(i) + 12)
		if chr(ord(i) ^ 5) in table:
			pad2[6] = chr(ord(i) ^ 5)
			if chr(ord(i) ^ 15) in table:
				pad2[0] = chr(ord(i) ^ 15)
				if chr(187 - (ord(i) ^ 15)) in table:
					pad2[4] = chr(187 - (ord(i) ^ 15))
					if chr(210 - (ord(i) ^ 15)) in table:
						pad2[7] = chr(210 - (ord(i) ^ 15))
						if chr((ord(i) + 1)/2) in table:
							pad2[5] =  chr((ord(i) + 1)/2)
							if chr((ord(i) + 12) ^ 47) in table:
								pad2[2] = chr((ord(i) + 12) ^ 47)
								print pad2,ord(pad2[2]) - 4 ^ 113

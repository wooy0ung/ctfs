#!/usr/bin/python
# -*- coding:utf8 -*-

s = [113, 123, 118, 112, 108, 94, 99, 72, 38, 68, 72, 87, 89, 72, 36, 118, 100, 78, 72, 87, 121, 83, 101, 39, 62, 94, 62, 38, 107, 115, 106]

v0 = []
for i in range(len(s)):
	v0.append(s[i] ^ 23)

print v0

flag = ""
for i in v0:
	flag += chr(i)

print flag
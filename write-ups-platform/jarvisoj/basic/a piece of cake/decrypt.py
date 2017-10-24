#!/usr/bin/python
#encoding:utf-8

import sys

FILENAME = 'encrypt.txt'

chart = 'abcdefghijklmnopqrstuvwxyz'
letters = 'abdefgijklmnpqrstuvwxyz'
dest_str = list('etaoinshrdlcumwfgypbvkjxqz')
dict_count = 0
letter_num = 23
dict = {}
freq_dict = {}
 
def get_freq(encrypt_str):
    for letter in encrypt_str:
    	if letter < 'A' or (letter >'Z' and letter < 'a') or letter > 'z':
    		continue 
        freq_dict[letter]=freq_dict.get(letter,0)+1

def print_dict():
	print "----------------------------"
	print "|           dict           |"
	print "----------------------------"
	for i in range(0,dict_count):
		print "[ %c -> %c ]" % (freq_dict[i][0], dict[freq_dict[i][0]])
	print ""

def init_dict(freq_dict,dest_str):
	global dict_count
	for i in range(26):
		dict[chr(ord('a')+i)] = chr(ord('a')+i)
	dict[','] = ','
	dict[':'] = ':'
	dict['-'] = '-'
	dict['.'] = '.'
	dict[' '] = ' '

	dict[freq_dict[0][0]] = dest_str[0]
	dict[freq_dict[1][0]] = dest_str[1]
	dest_str[0] = '0'
	dest_str[1] = '0'
	dict_count = 2
	print_dict()

def decrypt():
	print "----------------------------"
	print "|          decrypt         |"
	print "----------------------------"
	for i in range(len(encrypt_str)):
		sys.stdout.write(dict[encrypt_str[i]])
	print ""
	print ""

def guess():
	global dict_count

	while True
		while True:
			print "choose: %c -> [ " % freq_dict[dict_count][0],
			for i in range(26):
				if dest_str[i] == '0':
					continue
				print "%c" % dest_str[i],
			print " ] ?"

			ch = raw_input("input: ")
			dict[freq_dict[dict_count][0]] = ch
			dict_count = dict_count + 1
			print_dict()
			decrypt()
			print "press [y] for next letter, or [n] to retry..."
			select = raw_input("input: ")
			print ""
			if select == 'y':
				dest_str[dest_str.index(ch)] = '0'
				break
			dict_count = dict_count - 1
		if freq_dict[dict_count-1][0] == 'p':
			break;
	print ""
	print "may be you successfully decrypt!!!"


encrypt_str = open(FILENAME,'r').read()
print "----------------------------"
print "|          encrypt         |"
print "----------------------------"
print encrypt_str
print ""

get_freq(encrypt_str)
freq_dict = sorted(freq_dict.items(), key = lambda d: d[1], reverse=True)
print "----------------------------"
print "|         frequency        |"
print "----------------------------"
for i in range(len(freq_dict)):
	print '%s: %d' % (freq_dict[i][0],freq_dict[i][1])
print ""

init_dict(freq_dict, dest_str)
guess()
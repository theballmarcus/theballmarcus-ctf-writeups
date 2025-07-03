# Secret Portal - Pwn
My only solve for this 5 hour competition! (Not to complain, but all challenges gave the same amount of points even though 2 of the crypto was easily solved with AI) :)

Description:
``` 
I was too broke to afford an actual car, so I decided to make this app to simulate a carpark instead...

Author: elijah5399
    
Example Flag Format: ICO{xxxxxxx}

nc ico-carpark.nusgreyhats.org 80

backup: nc ico.nusgreyhats.org 33102
```

While looking through the code, you might notice that there will be allocated 10 bytes for it. But we can change index 10, which means there is off-by-one vuln.
```cpp
struct Carparks {
    ll carpark1[CARPARK1_SPACE];
    vector<ll> carpark2 = vector<ll>(CARPARK2_SPACE, 0); 
};
        ...
            if (slot < 0 || slot > CARPARK1_SPACE) {
                puts("Invalid slot!");
                continue;
            }
        ...
    }
``` 
Hence, we can overwrite the address for the second carpark. That means that we can write and read arbitrarily in memory. The executeable is compiled with --no-pie, so the addresses are not random, and we can therefore leak libc addresess. At first, I didn't realise we had gotten a Dockerfile and could find the libc version using that, so I leaked 4 different function addreses and put them into [libc.rip](https://libc.rip/)
First I would find the GOT entry for a function: `readelf -r chall`
Second, I could overwrite the second car park with the address and read the libc address:
```py
printf_addr = 0x404020
change_carpark1(10, printf_addr)  
leaked_printf = view_carpark2(0)
print(f"Leaked printf@libc: {hex(leaked_printf)}")
```

```
Leaked printf@libc: ...
Leaked puts@libc: ...
Leaked set_vbuf@libc: ...
Leaked setbuf@libc: ...
```
Putting the functions and offsets into [libc.rip](https://libc.rip/) gave me these possible libc versions:
```
libc6_2.35-0ubuntu3.10_amd64.so  libc6_2.35-0ubuntu3.7_amd64.so
libc6_2.35-0ubuntu3.4_amd64.so   libc6_2.35-0ubuntu3.8_amd64.so
libc6_2.35-0ubuntu3.5_amd64.so   libc6_2.35-0ubuntu3.9_amd64.so
libc6_2.35-0ubuntu3.6_amd64.so
``` 
I then enumerated them and found out every one of them had the exact same one_gadget addresses by running `one_gadget --raw libc...`
I then cleaned up my python script and wrote `clean.py` that tries every single one_gadget using and uses a specific libc file for offset comparison. (Of course this would be unecesarry if I had gotten the exact libc version from the docker container)
`clean.py` got me the flag

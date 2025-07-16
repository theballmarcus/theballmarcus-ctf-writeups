# Safe Gets

**Challenge Description**:
I think I found a way to make gets safe.

**Points**:
50

**Solution**:
I first noticed that the `chall` doesn't have a PIE and canary. It has a `gets` function which reads into a `BUF[259]` which is unsafe. However, the wrapper does have a input limit which is the same size as the buffer that `chall` reads into. That means it's safe, right? 
Definitely not.
```python
payload = input(f"Enter your input (max {MAX_LEN} bytes): ")
if len(payload) > MAX_LEN:
    print("[-] Input too long!")
    sys.exit(1)
print(len(payload))
# Start the binary with pipes
proc = subprocess.Popen(
    [BINARY],
    stdin=subprocess.PIPE,
    stdout=sys.stdout,
    stderr=subprocess.PIPE
)

try:
    # Send initial payload
    proc.stdin.write(payload.encode() + b'\n')
    proc.stdin.flush()
```
The payload length is read before it is encoded - and it happens that we can send unicode characters, which will count as 1 length before it's encoded and 4 after it is. That means we can fill the buffer and make a classic buffer overflow.
We can send a payload consisting of a lot of `😊` which will expand to 4 bytes. After that, we can overwrite the return address to a `win` function inside the binary.
[Solution script](exploit.py)
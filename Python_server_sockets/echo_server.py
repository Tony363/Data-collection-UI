#!/usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT =  65432      # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
   
    try:
        s.bind((HOST, PORT))        
        s.settimeout(4)
        s.listen()
    except socket.timeout:
        # s.close()
        print('no client received')
    
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    
        
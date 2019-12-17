import random
import socket
import sys
import os
import time


def udp_socket(index):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', 12000))
    print('waiting for udp client')
    
   
    try:
        while True:
            server_socket.settimeout(10)
        
            
            message, address = server_socket.recvfrom(1024)
            print('client received: {}'.format(address))
            # message = message.upper()
          
            send_message = bytes('connection established: index {}'.format(index), encoding='utf-8')
            print(message)
            
            server_socket.sendto(send_message, address)
    except socket.timeout:
        print('exceeded time')
        server_socket.close()
    except KeyboardInterrupt:
        print('time to close udp server')
        server_socket.shutdown(socket.SOCK_DGRAM)
        sys.exit(1)

# udp_socket()
            
 
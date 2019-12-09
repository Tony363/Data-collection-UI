import random
import socket
import sys
import os

# def main():
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))
print('waiting for udp client')
server_socket.settimeout(5)

while True:
    try:
       
        message, address = server_socket.recvfrom(1024)
        print('client received: {}'.format(address))
        # message = message.upper()
        send_message = b'connection established'
        print(message)
        
        server_socket.sendto(send_message, address)
    except KeyboardInterrupt:
        print('time to close udp server')
        server_socket.shutdown(socket.SOCK_DGRAM)
        sys.exit(1)
        
            


# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
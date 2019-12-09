import random
import socket
import sys
import os

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', 12000))

    # for i in range(5):
    while True:
        try:
            # rand = random.randint(0, 10)
            message, address = server_socket.recvfrom(1024)
            # message = message.upper()
            message = b'message returned'
            print(message)
            print(address)
            # if rand >= 4:
            server_socket.sendto(message, address)
        except KeyboardInterrupt:
            server_socket.shutdown(socket.SOCK_DGRAM)
            sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
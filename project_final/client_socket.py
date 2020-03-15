

def client(table):
    i = 0
    while i < 2:
        print(table)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(1.0)
        message = b'test'
        addr = ("127.0.0.1", 12000)

        start = time.time()
        # client_socket.sendto(message, addr)

        byte = json.dumps(table,indent=2).encode('utf-8')
        client_socket.sendto(byte, addr)
        try:
            data, server = client_socket.recvfrom(1024)
            end = time.time()
            elapsed = end - start
            print(f'{server} {data} {elapsed}')
            # time.sleep(1)
        except socket.timeout:
            print('REQUEST TIMED OUT')
            time.sleep(1)
            i += 1

    # return client_socket


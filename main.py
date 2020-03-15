from arcade_games import triangle2
from Python_server_sockets.udp_client import client

def controller():
    print(triangle2.main(client()))
    # triangle2.main(1)
    
controller()

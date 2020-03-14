from arcade_games import triangle2
from Python_server_sockets import udp_client

def controller():
    print(triangle2.main(udp_client.main()))
    # triangle2.main(1)
    
controller()

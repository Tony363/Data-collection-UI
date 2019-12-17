import threading
from udp_server import udp_socket


while True:
	try: 
		udp_socket()
		threading._start_new_thread(on_new_client,(client, ip))
	except KeyboardInterrupt:
		print(f"Gracefully shutting down the server!")
	except Exception as e:
		print(f"Well I did not anticipate this: {e}")
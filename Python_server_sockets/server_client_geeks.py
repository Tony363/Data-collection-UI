# first of all import the socket library 
import socket   
import sys  
import os           
  
# next create a socket object 
s = socket.socket()          
print ("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print ("socket is listening"  )          
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
    # Establish connection with client. 
    c, addr = s.accept()      
    print ('Got connection from', addr )
    try:

        message = c.recv(1024).decode()
        
        print(message)
        # send a thank you message to the client.  
        c.send(b'Thank you for connecting') 
    except KeyboardInterrupt:
        print('time to close socket')

        # shut every thing down
        s.close()
        c.close() 

        sys.exit(1)
  
   

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
import logging
import threading
import datetime
from threading import Lock, Thread
from udp_server import udp_socket

Lock = Lock()

def printitem(string, name):
    print(datetime.datetime.now().time(), string,name)

def thread_function(name,n):

    logging.info("Thread %s: starting", name)
    logging.info("Thread %s: finishing", name)

    for i in range(n):
        Lock.acquire()
        # time.sleep(3)
        
        printitem('This is Thread ',name)
        udp_socket()

        Lock.release()
        



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(thread_function(index,index))
        threads.append(x)
        x.start()
     

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
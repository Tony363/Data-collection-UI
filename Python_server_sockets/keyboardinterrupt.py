import time
import sys
import os
def main():
    for i in range(100):
        time.sleep(1)
        print(time.clock())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
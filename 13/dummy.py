import time
import threading

from requests.packages import target


def write_hello():
    while True:
        print("Hello World")
        time.sleep(2)

thread_hello=threading.Thread(target=write_hello)
thread_hello.start()

print("to je to")
import socket
from queue import Queue
import threading

ip_addr = input("Enter Ip address: ")
queue = Queue()
open_ports = []


def Socket(port):
    try:
        connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connector.connect((ip_addr, port))
        return True
    except:
        return False


def queuing(port_lists):
    for port in port_lists:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if Socket(port):
            print("open ports {}".format(port))
            open_ports.append(port)


port_list = range(1, 1024)
queuing(port_list)

thread_list = []

for i in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("open ports are", open_ports)

# This is programm examines which ports are open in a given network
# To run it please use the 'network' virtual environment for python

import socket 
import threading
from queue import Queue

def portscan(port, target = "127.0.0.1"):
    try:
        # Create the socket object
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.connect((target, port))
        return True
    except:
        return False

# Prepare a queue for the threading
# Without queue the ports will not be tested in order
def fill_queue(port_list, queue):
    for port in port_list:
        queue.put(port)

def main_operation(queue, target, open_ports):
    while not queue.empty():
        port = queue.get()
        if portscan(port, target):
            print("Print {} is open! ".format(port))
            open_ports.add(port)

# Main section
thread_queue = Queue()      # Used for queueing the results of the threads
target = input("Specify a target IP for scaning [IPv4] > ")
port_list = range(1,1025)   # The number of ports we want scanned
thread_list = []            # Used for thread administration
open_ports = []             # List of all open ports

fill_queue(port_list, thread_queue)

# Create the threads
for this_thread in range(10):
    thread = threading.Thread(target=main_operation, args=(thread_queue, target, open_ports)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()


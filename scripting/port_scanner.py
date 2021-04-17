import threading 
import time 

def function_name():
    print ('Firs thread')

# Thread object 

x = threading.Thread(target=function_name)
x.start()
print(threading.activeCount())

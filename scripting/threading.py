import threading 
import time

ls = []

def count(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)

def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)

# Thread object - x
x = threading.Thread(target=count)
x.start()

# Thread object - y
#y = threading.Thread(target = count2, args = (5,))
#y.start()

print(ls)

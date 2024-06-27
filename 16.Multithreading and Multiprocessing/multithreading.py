## Multithreading
# When to use Multi threading
## I/O bound task:Task that spend more time waing for I/O operaion(eg. fileoperation, networkrequsets)
## ConcurrentExecution:when you wnat to improve the throught of your application by performingmultiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'Number:{i}')

def print_letters():
    for i in 'abcde':
        time.sleep(2)
        print(f'Letters:{i}')

#create 2 threads
t1=threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t=time.time()
#start the thread
t1.start()
t2.start()

##wait for the threads to complete
t1.join()
t2.join()
finished_time = time.time() - t
print(finished_time)
### Multithreading With Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time


def print_numbers(number):
    time.sleep(1)
    return f'Numbers:{number}'

number=[1,2,3,4,5,4,7,8,9,6,10,45,7,8,3,6,4,8,9]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_numbers,number)

for i in results:
    print(i)
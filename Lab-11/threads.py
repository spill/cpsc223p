# Write a Python program that creates two threads. One thread should print even numbers from 1 to 10, and the other thread should print odd numbers from 1 to 10. Ensure that the output from both threads is synchronized such that the output appears in the correct order.

# Hint: Start with threading module to create two threads, one for printing even numbers and another for printing odd numbers. A Lock object should be used to synchronize the threads. Each thread acquires the lock before printing its number, ensuring that the output appears in the correct order.

# Make sure to use at least each of the following function - Lock(), join(), acquire(), release() in the code implementation.

import threading

def print_even(lock):
    for num in range(1, 11):
        if num % 2 == 0:
            lock.acquire()  
            print(num)
            lock.release()  

def print_odd(lock):
    for num in range(1, 11):
        if num % 2 != 0:
            lock.acquire()  
            print(num)
            lock.release()  
if __name__ == "__main__":
    lock = threading.Lock()  

    thread_even = threading.Thread(target=print_even, args=(lock,))
    thread_odd = threading.Thread(target=print_odd, args=(lock,))

    thread_odd.start()
    thread_even.start()

    thread_odd.join()
    thread_even.join()

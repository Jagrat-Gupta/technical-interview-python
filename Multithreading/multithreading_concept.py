"""
Multithreading in Python allows you to run multiple threads (smaller units of a process) concurrently, which can help improve the performance of your program, 
especially for I/O-bound tasks. Here are some key concepts:
1. Threads and Processes

    Thread: The smallest unit of execution within a process. Threads share the same memory space, making communication between them more efficient.
    Process: A program in execution with its own memory space. Processes are more isolated from each other compared to threads.

2. Global Interpreter Lock (GIL)

Python Global Interpreter Lock (GIL) ensures that only one thread executes Python bytecode at a time. This means that even in a multithreaded Python program, only one 
thread can execute Python code at once. This can be a limitation for CPU-bound tasks but is less of an issue for I/O-bound tasks1.

3. Creating and Starting Threads

You can create and start threads using the threading module:
'''
import threading

def print_numbers():
    for i in range(10):
        print(i)

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()
'''

To avoid conflicts when multiple threads access shared resources, you can use synchronization primitives like locks, semaphores, and events:

    Locks: Ensure that only one thread can access a resource at a time.
    Semaphores: Allow a fixed number of threads to access a resource.
    Events: Allow threads to wait for certain conditions to be met.

5. Thread Safety

Ensuring thread safety is crucial to avoid race conditions and other concurrency issues. Using immutable objects and proper synchronization techniques can help achieve thread safety2.
6. Advanced Concepts

    Daemon Threads: These are background threads that automatically terminate when the main program exits.
    ThreadPoolExecutor: A high-level interface for managing a pool of threads to execute tasks concurrently.




"""

import threading

def print_numbers():
    for i in range(10):
        print(i)

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()


#https://www.youtube.com/watch?v=IEEhzQoKtQU&t=1269s
"""
A **race condition** occurs when two or more threads access shared data and try to change it at the same time, leading to unpredictable results. 
Here’s a more detailed explanation:

### What is a Race Condition?
- **Definition**: A race condition happens when the outcome of a program depends on the sequence or timing of uncontrollable events such as thread execution order¹.
- **Example**: Imagine two threads trying to increment a shared counter variable. If both threads read the same initial value, increment it, and then write back 
the result, the final value will be incorrect because one increment operation will be lost.

### Why Do Race Conditions Occur?
- **Concurrent Access**: When multiple threads access and modify shared data without proper synchronization, race conditions can occur².
- **Timing Issues**: The exact timing of thread execution can vary, leading to different outcomes each time the program runs³.

### Example in Python
Here’s a simple example to illustrate a race condition:

```python
import threading

counter = 0

def increase(by):
    global counter
    local_counter = counter
    local_counter += by
    counter = local_counter

# Creating threads
thread1 = threading.Thread(target=increase, args=(10,))
thread2 = threading.Thread(target=increase, args=(20,))

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

print(f'The final counter is {counter}')
```

In this example, both threads try to modify the `counter` variable at the same time. The final value of `counter` depends on which thread completes its update last, leading to unpredictable results¹.

### Preventing Race Conditions
- **Locks**: Use threading locks (mutexes) to ensure that only one thread can access the shared resource at a time¹.
- **Atomic Operations**: Use atomic operations that are indivisible and ensure that a variable is updated correctly without interruption².

Would you like to see an example of how to use locks to prevent race conditions?

¹: [Python Tutorial](https://www.pythontutorial.net/python-concurrency/python-threading-lock/)
²: [Super Fast Python](https://superfastpython.com/thread-race-condition-shared-variable/)
³: [GeeksforGeeks](https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/)

"""

import threading

counter = 0

def increase(by):
    global counter
    local_counter = counter
    local_counter += by
    counter = local_counter

# Creating threads
thread1 = threading.Thread(target=increase, args=(10,))
thread2 = threading.Thread(target=increase, args=(20,))

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

print(f'The final counter is {counter}')
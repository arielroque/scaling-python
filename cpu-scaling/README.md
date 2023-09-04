# CPU Scaling

As CPUs are not getting infinitely faster, using multiple CPUs is the best path towards scalability. That means introducing concurrency and parallelism into your program. This is not an easy task. However, once correctly done, it really does increase the total throughput.

## Threads
Scaling across processors is usually done using multithreading. Multithreading is the ability to run code in parallel using threads. Threads are usually provided by the operating system and are contained in a single process. The operating system is responsible for scheduling their execution.

Threads in Python are a good way to run a function concurrently with other functions. If your system does not support multiple processors, the threads will be executed one after another as scheduled by the operating system. However, if multiple CPUs are available, threads could be scheduled on multiple processing units, once again as determined by the operating system.

```bash
# Run the threads program
python3 threads.py
```

**However**, this does have several drawbacks in Python. If you have been in the Python world for a long time, you have probably encountered the word GIL, and know how hated it is. The GIL is the Python global interpreter lock, a lock that must be acquired each time CPython needs to execute byte-code. Unfortunately, this means that if you try to scale your application by making it run multiple threads, **this global lock always limits the performance** of your code, as there are many conflicting demands. All your threads try to grab it as soon as they need to execute Python instructions.

The reason that the GIL is required in the first place is that it makes sure that some basic Python objects are thread-safe. For example, the code in the following example would not be thread-safe without the global Python lock.

```bash
import threading

x = []

def append_two(l):
  l.append(2)

threading.Thread(target=append_two, args=(x,)).start()
x.append(1)
print(x)
```

## Processes 

Since multithreading is not a perfect scalability solution because of the Global Interpreter Lock (GIL), using processes instead of threads is a good alternative. Python obviously exposes the OS fork system call to create new processes. However, in most cases, this approach is a little bit too low-level to be interesting.

```bash
# Run the processes program
python3 processes.py
```

## Futures




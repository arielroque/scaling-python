import threading

def print_something(something):
    print(something)

thread = threading.Thread(target=print_something,args=("hello",))
thread.start()

print("Thread started")

thread.join() # Join is important because the application
              # will wait until the thread finished
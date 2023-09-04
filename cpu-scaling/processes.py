import random 
import multiprocessing

def compute(results):
    results.append(sum([random.randint(1,100) for i in range(1000000)]))

with multiprocessing.Manager() as manager:
    results = manager.list() # create an list that will be shared with other processes
    workers = [multiprocessing.Process(target=compute,args=(results,)) for x in range(8)] # create 8 processes

    for worker in workers:
        worker.start()
    
    for worker in workers:
        worker.join() # The main program will wait the child processes to finish
    
    print("Results %s" %results)
    

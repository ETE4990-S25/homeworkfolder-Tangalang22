from datetime import datetime, timedelta
import multiprocessing
from math import factorial
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_prime(time):
    end_time = datetime.now() + timedelta(minutes = time)
    x = 0 #start of prime iterator
    while datetime.now() < end_time:
        prime_check = is_prime(x)
        if prime_check == True:
            prime = x
        x += 1
    return prime

def find_fib(queue, optimusprime):
    a = 0
    b = 1
    c = 0
    fib = 0
    while fib < optimusprime:
        fib = a + b
        c = a #c is for the final result because fib would return one iteration above what i wanted
        a = b
        b = fib
        if b > 1e8:  # Was running into issues of the program running for forever, asked chatgpt and they said to put limits
            queue.put("Fibonacci hit safety limit")
            return
    queue.put(f"Fibonacci is: {fib - c}")
    print("Fibonacci process finished", flush=True)

def find_fact(queue, optimusprime):
    factbase = 0
    factresult = 0
    while factresult < optimusprime:
        factresult = factorial(factbase)
        if factresult >= optimusprime:
            break
        if factresult > 1e12:  # another limit from chatgpt
            queue.put("Factorial hit safety limit")
            return
        factbase += 1
    queue.put(f"Factorial is: {factorial(factbase-1)}. Factorial base is: {factbase-1}")
    print("Factorial process finished", flush=True)

#optimusprime = find_prime(1) These are all tests to make sure the math side works.
#print("prime is: ", optimusprime)
#fibonacci = find_fib()
#print("fibonacci is: ", fibonacci)
#fact_prime = find_fact()
#print("factorial is: ", fact_prime)


if __name__ == '__main__':
    start = time.perf_counter()
    optimusprime = find_prime(3)
    print("Prime is:", optimusprime) #i named the final prime variable optimus prime because it was easy to remember
    manager = multiprocessing.Manager()
    queue = manager.Queue()
    
    p1 = multiprocessing.Process(target = find_fib, args = (queue, optimusprime))
    p2 = multiprocessing.Process(target = find_fact, args = (queue, optimusprime))
    
    print("Starting processes...")
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    print("Processes finished. Reading results from the queue:")
    

    for _ in range(2):
        result = queue.get(timeout=5)  # Another time limit to prevent program from timing out, idky it worked in a py file but not in jupyter
        print(result)
    
    processtime = time.perf_counter()
    print("Finished job in: ", processtime/100000, "seconds")

#Terminal output 
# Prime is: 24391781
#Starting processes...
#Fibonacci process finished
#Factorial process finished
#Processes finished. Reading results from the queue:
#Fibonacci is: 24157817
#Factorial is: 3628800. Factorial base is: 10
#Finished job in:  0.722555061084 seconds
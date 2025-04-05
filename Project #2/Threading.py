from datetime import datetime, timedelta
import threading
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

def find_fib():
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
            print("Fibonacci hit safety limit")
            return
    print(f"Fibonacci is: {fib - c}")
    print("Fibonacci process finished", flush=True)

def find_fact():
    factbase = 0
    factresult = 0
    while factresult < optimusprime:
        factresult = factorial(factbase)
        if factresult >= optimusprime:
            break
        if factresult > 1e12:  # another limit from chatgpt
            print("Factorial hit safety limit")
            return
        factbase += 1
    print(f"Factorial is: {factorial(factbase-1)}. Factorial base is: {factbase-1}")
    print("Factorial process finished", flush=True)

if __name__ == '__main__':
    start = time.perf_counter()
    optimusprime = find_prime(3)
    print("Prime is:", optimusprime) #i named the final prime variable optimus prime because it was easy to remember
    
    print("Starting processes...")
    thread1 = threading.Thread(target = find_fib)
    thread2 = threading.Thread(target = find_fact)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Processes finished. Reading results from the queue:")
    
    processtime = time.perf_counter()
    print("Finished job in: ", processtime/100000, "seconds")

#Terminal Output
#Prime is: 24876673
#Starting processes...
#Fibonacci is: 24157817
#Fibonacci process finished
#Factorial is: 3628800. Factorial base is: 10
#Factorial process finished
#Processes finished. Reading results from the queue:
#Finished job in:  0.8675553931969999 seconds
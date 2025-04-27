from datetime import datetime, timedelta
import asyncio
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

async def find_fib(optimusprime, starttime):
    a = 0
    b = 1
    fib = 0
    count = 0
    while fib <= optimusprime:
        fib = a + b
        a = b
        b = fib
        if b > 1e8:  # Was running into issues of the program running for forever, asked chatgpt and they said to put limits
            print("Fibonacci hit safety limit")
            return
        count += 1
    fib_time = time.time() - starttime
    print(f"Fibonacci is: {a}. Fibonacci base: {count}. It took {fib_time} seconds to find this number.")
    print("Fibonacci process finished", flush=True)

async def find_fact(optimusprime, starttime):
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
    fact_time = time.time() - starttime
    print(f"Factorial is: {factorial(factbase-1)}. Factorial base is: {factbase-1}. It took {fact_time} seconds to find this number.")
    print("Factorial process finished", flush=True)

async def main():
    optimusprime = find_prime(3)
    print("Prime is:", optimusprime) #i named the final prime variable optimus prime because it was easy to remember
    starttime = time.time()
    print("Starting processes...")
    output = await asyncio.gather(
        find_fib(optimusprime, starttime),
        find_fact(optimusprime, starttime)
    )
    print("Processes finished.")

asyncio.run(main())

#Terminal Output
#Prime is: 24862511
#Starting processes...
#Fibonacci is: 24157817. Fibonacci base: 37. It took 0.00019693374633789062 seconds to find this number.
#Fibonacci process finished
#Factorial is: 3628800. Factorial base is: 10. It took 0.0003056526184082031 seconds to find this number.
#Factorial process finished
#Processes finished.
#
#For context, my CPU has 12 cores and 24 threads.
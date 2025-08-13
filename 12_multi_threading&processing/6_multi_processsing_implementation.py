### Calculating the factorial of a large numbers
# The factorial of a number is the product of all positive integers less than or equal to that number.
import multiprocessing
import time
import sys
import math

## set int max str digits
sys.set_int_max_str_digits(100000)

## Definig the function
def compute_factorial(numbers):
    print(f"The factorials are being calculated")
    result=math.factorial(numbers)
    print(f"Factorial of the number {numbers} is {result}")
    return result

start_time=time.time()

## Multi-processing
if __name__ == '__main__':
    numbers=(1000,2000,3000)
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)
    
    end_time=time.time()-start_time
    print(f"Time taken is {end_time}")




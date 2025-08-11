from concurrent.futures import ThreadPoolExecutor
import time

numbers=[1,2,3,4,5]

def print_numbers(numbers):
    time.sleep(1)
    return f"Number : {numbers}"

t=time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_numbers,numbers)

for result in results:
    print(result)

finished_time= time.time()-t
print(finished_time)

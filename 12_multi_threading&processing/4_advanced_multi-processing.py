from concurrent.futures import ProcessPoolExecutor
import time

numbers=[1,2,3,4,5,6]
def sqr(numbers):
    time.sleep(1)
    return numbers*numbers

t=time.time()
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(sqr, numbers)

    for result in results:
        print (result)

finished_time=time.time()-t
print (f"Finished time:{finished_time}")

        
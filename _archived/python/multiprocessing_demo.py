#!/usr/bin/python
"""Multiprocessing demo."""
# Jak Crow
# Created: 2018/02/03

from multiprocessing import cpu_count, Pool, Process, Queue
import random
import sys
import time

random.seed()
def generate_list(size):
    random_list = [random.randint(0, 10) for _ in range(size)]
    return random_list

def sum_list(list_):
    final_sum = 0
    for value in list_:
        final_sum = final_sum + value
    return final_sum

def do_work_queue(N, queue):
    my_list = generate_list(N)
    final_sum = sum_list(my_list)
    queue.put(final_sum)

def do_work_pool(N):
    my_list = generate_list(N)
    final_sum = sum(my_list)
    return final_sum

def square(x):
    return x*x

if __name__ == '__main__':
    N = 10_000_000
    CORES = cpu_count()
    start_time = time.time()

    # # Using manual processes and queues
    # queue = Queue()
    # processes = [Process(target=do_work_queue, args=(int(N/CORES), queue)) for _ in range(CORES)]
    # [process.start() for process in processes]
    # partial_results = [queue.get() for _ in range(CORES)]
    # final_sum = sum_list(partial_results)

    # Using pools
    data = [int(N/CORES) for _ in range(CORES)]
    with Pool(processes=CORES) as pool:
        partial_results = pool.map(do_work_pool, data)
    final_sum = sum(partial_results)

    end_time = time.time()
    print(f"{CORES} processes, {end_time - start_time} seconds")
    print(f"The final sum was: {final_sum}")

# ─────────────────────────────────────────────────────────────────────────────
    # How map_async works
    import multiprocessing as mp
    import time

    def square(x):
        return x*x

    start_time = time.time()
    CORES = mp.cpu_count()
    parameters = list(range(50000000))
    pool = mp.Pool(processes=8)

    results = []
    r = pool.map_async(square, parameters, callback=results.extend)
    while True:
        time.sleep(1)
        if r.ready():
            break
        else:
            print(r.ready())

    print(f"finished in {(time.time() - start_time):.2f} seconds")

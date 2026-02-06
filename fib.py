import time
import functools
import matplotlib.pyplot as plt

@functools.lru_cache(None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    max_n = 100
    ns = []
    times = []

    fib.cache_clear()               # 1️⃣ clear cache once
    start = time.perf_counter()     # 2️⃣ start total timer

    for n in range(1, max_n + 1):
        fib(n)                      # 3️⃣ compute next fib
        elapsed_time = time.perf_counter() - start
        ns.append(n)
        times.append(elapsed) #add new elapsed time 'times' list
        print(f"n={n}, total time={elapsed_time:.6f}s")

    plt.plot(ns, times, marker='o')
    plt.xlabel("n")
    plt.ylabel("Total computation time (s)")
    plt.title("Total Fibonacci Computation Time with Caching")
    plt.grid(True)
    plt.show()


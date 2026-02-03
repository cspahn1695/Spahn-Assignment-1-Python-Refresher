import time
import functools
import matplotlib.pyplot as plt

@functools.lru_cache(None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def time_fib(n: int) -> float:
    fib.cache_clear()          # IMPORTANT for fair timing
    start = time.perf_counter()
    fib(n)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    max_n = 40                 # adjust if needed
    ns = []
    times = []

    for n in range(1, max_n + 1):
        t = time_fib(n)
        ns.append(n)
        times.append(t)
        print(f"finished in {t:.8f}s, f({n:2d})={fib(n)}")

    # Plot
    plt.figure()
    plt.plot(ns, times, marker='o')
    plt.xlabel("n (largest Fibonacci index)")
    plt.ylabel("Time to compute fib(n) [seconds]")
    plt.title("Fibonacci Computation Time vs n")
    plt.grid(True)
    plt.show()
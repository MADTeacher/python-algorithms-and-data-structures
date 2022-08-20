import time


def o_n(n: int) -> None:
    tic = time.perf_counter()
    count = 0
    for i in range(0, n):
        count += 1
    toc = time.perf_counter()
    print(f"O(n): {toc - tic:0.4f}")


def o_n2(n: int) -> None:
    tic = time.perf_counter()
    count = 0
    for i in range(0, n):
        for j in range(0, n):
            count += 1
    toc = time.perf_counter()
    print(f"O(n^2): {toc - tic:0.4f}")


def o_log_n(n: int) -> None:
    tic = time.perf_counter()
    count = 0
    i = 0
    while i < n:
        count += 1
        i += 1
    toc = time.perf_counter()
    print(f"O(log n): {toc - tic:0.4f}")


def o_n_v2(n: int) -> None:
    tic = time.perf_counter()
    count = 0
    for i in range(0, n):
        count += 1
    for i in range(0, n):
        count += 1
    toc = time.perf_counter()
    print(f"O(n): {toc - tic:0.4f}")


def o_n_v3(n: int) -> None:
    tic = time.perf_counter()
    count = 0
    k = 0
    for i in range(0, n):
        while k < n:
            count += 1
            k += 1
    toc = time.perf_counter()
    print(f"O(n): {toc - tic:0.4f}")


if __name__ == '__main__':
    n = 10000  # O(1)
    o_n(n)
    o_n_v2(n)
    o_n_v3(n)
    o_n2(n)
    o_log_n(n)

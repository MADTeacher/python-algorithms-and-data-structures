
dp: list[int] = [0 for _ in range(0, 1000)]


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    if dp[n] > 2:
        return dp[n]

    k = 0
    if n & 1 > 0:
        k = (n+1)//2
    else:
        k = n // 2

    if n & 1 > 0:
        dp[n] = fibonacci(k)*fibonacci(k) + fibonacci(k-1)*fibonacci(k-1)
    else:
        dp[n] = (2*fibonacci(k-1) + fibonacci(k)) * fibonacci(k)

    return dp[n]


if __name__ == "__main__":
    print(fibonacci(20))


def find_min_squares(n: int) -> int:
    dp: list[int] = [0 for _ in range(0, n + 1)]
    for i in range(0, n + 1):
        dp[i] = i
        j = 1
        while j*j <= i:
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j += 1
    return dp[n]


if __name__ == "__main__":
    print(find_min_squares(20))  # 2
    print(find_min_squares(10))  # 2
    print(find_min_squares(96))  # 3
    print(find_min_squares(100))  # 1

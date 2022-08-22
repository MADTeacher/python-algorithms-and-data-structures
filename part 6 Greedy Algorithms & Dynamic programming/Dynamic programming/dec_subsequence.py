
if __name__ == "__main__":
    array: list[int] = [0, 2, 1, 30, 9, 8, -3, -5, 6, 8, 15, 20, 0, 5]
    dp: list[int] = [0 for _ in range(0, len(array))]
    max_value = temp_max = 0

    dp[0] = 1
    for i in range(1, len(array)):
        dp[i] = 1
        for j in range(0, i):
            if array[i] < array[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
            if dp[i] > temp_max:
                temp_max += 1
            else:
                if temp_max > max_value:
                    max_value = temp_max
                temp_max = 0

    print(dp, max_value)

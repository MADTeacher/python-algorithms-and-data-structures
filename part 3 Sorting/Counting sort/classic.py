def find_max_min(array: list[int]) -> tuple[int, int]:
    if len(array) == 0:
        raise ValueError("array is empty")

    a_min = float("inf")
    a_max = float("-inf")
    for v in array:
        if a_max < v:
            a_max = v
        if a_min > v:
            a_min = v
    return a_min, a_max


def counting_sort(array: list[int]) -> None:
    if len(array) == 0:
        raise ValueError("array is empty")

    a_min, a_max = find_max_min(array)
    array_counts = [0 for _ in range(a_max - a_min + 1)]

    for it in arr:
        array_counts[it - a_min] += 1

    it = 0
    for idx, count in enumerate(array_counts):
        while count > 0:
            array[it] = idx + a_min
            it += 1
            count -= 1


if __name__ == '__main__':
    arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
    print(f"Array before sort: {arr}")
    counting_sort(arr)
    print(f"Array after sorting: {arr}")

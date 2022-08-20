def get_max(arr: list[int]) -> int:
    a_max = float("-inf")
    for v in arr:
        if a_max < v:
            a_max = v
    return a_max


def radix_sort(arr: list[int]) -> list[int]:  # ToDo Нет comp ...
    if len(arr) == 0:
        raise ValueError("array is empty")
    arr = arr.copy()
    dig_place = 1
    result = [0 for _ in range(len(arr))]

    max_number = get_max(arr)
    while max_number / dig_place > 0:
        count = [0 for _ in range(10)]  # частота чисел от 0 до 9
        for val in arr:
            count[(val // dig_place) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            result[count[(arr[i] // dig_place) % 10] - 1] = arr[i]
            count[(arr[i] // dig_place) % 10] -= 1

        arr = result.copy()
        dig_place *= 10

    return arr


arr = [1, 2, 6, 0, 362, 214, 22, 54, 109, 5, 3]
print(f"Array before sort: {arr}")
sortedArray = radix_sort(arr)
print(f"Array after sorting: {sortedArray}")

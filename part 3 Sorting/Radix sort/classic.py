def get_max(arr: list[int]) -> int:
    a_max = float("-inf")
    for v in arr:
        if a_max < v:
            a_max = v
    return a_max


def radix_sort(arr: list[int]) -> None: 
    if len(arr) == 0:
        raise ValueError("array is empty")
    
    buffer = arr.copy()
    dig_place = 1
    result = [0 for _ in range(len(arr))]

    max_number = get_max(buffer)
    while max_number / dig_place > 0:
        count = [0 for _ in range(10)]  # частота чисел от 0 до 9
        for val in buffer:
            count[(val // dig_place) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(buffer) - 1, -1, -1):
            result[count[(buffer[i] // dig_place) % 10] - 1] = buffer[i]
            count[(buffer[i] // dig_place) % 10] -= 1

        buffer = result.copy()
        dig_place *= 10
    for i in range(0, len(buffer)):
        arr[i] = buffer[i]


if __name__ == '__main__':
    arr = [1, 2, 6, 0, 362, 214, 22, 54, 109, 5, 3]
    print(f"Array before sort: {arr}")
    radix_sort(arr)
    print(f"Array after sorting: {arr}")


def bubble_sort(arr: list[int]) -> list[int]:
    if len(arr) == 0:
        raise ValueError("array is empty")
    arr: list[int] = arr.copy()

    def swap(i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap(j, j + 1)
    return arr


arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
sortedArray = bubble_sort(arr)
print(f"Array before sort: {arr}")
print(f"Array after sorting: {sortedArray}")

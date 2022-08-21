def bubble_sort(arr: list[int]) -> None:
    if len(arr) == 0:
        raise ValueError("array is empty")

    def swap(i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap(j, j + 1)


if __name__ == '__main__':
    arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
    print(f"Array before sort: {arr}")
    bubble_sort(arr)    
    print(f"Array after sorting: {arr}")

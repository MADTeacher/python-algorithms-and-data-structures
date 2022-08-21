from collections.abc import Callable


def selection_sort(arr: list[int], comp: Callable[[int, int], bool]) -> None:
    if len(arr) == 0:
        raise ValueError("array is empty")

    def swap(i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(0, len(arr)):
        min = i
        for j in range(i, len(arr)):
            if not comp(arr[j], arr[min]):
                min = j
        swap(i, min)


if __name__ == '__main__':
    arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
    arr_copy = arr.copy()
    print(f"Array before sort: {arr}")
    selection_sort(arr, lambda i, j: i > j)
    print(f"Array after ascending sorting: {arr}")
    selection_sort(arr_copy, lambda i, j: i < j)
    print(f"Array after descending sorting: {arr_copy}")

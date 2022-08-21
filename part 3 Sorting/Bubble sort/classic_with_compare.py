from collections.abc import Callable


def bubble_sort(arr: list[int], comp: Callable[[int, int], bool]) -> None:
    if len(arr) == 0:
        raise ValueError("array is empty")

    def swap(i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if comp(arr[j], arr[j + 1]):
                swap(j, j + 1)


if __name__ == '__main__':
    arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
    arr_clone = arr.copy()
    print(f"Array before sort: {arr}")
    bubble_sort(arr, lambda i, j: i > j)
    print(f"Array after ascending sorting: {arr}")
    bubble_sort(arr_clone, lambda i, j: i < j)
    print(f"Array after descending sorting: {arr_clone}")

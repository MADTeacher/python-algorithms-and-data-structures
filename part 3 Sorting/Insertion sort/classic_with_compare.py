from collections.abc import Callable


def insertion_sort(arr: list[int], comp: Callable[[int, int], bool]) -> None:
    if len(arr) == 0:
        raise ValueError("array is empty")

    for i in range(1, len(arr)):
        temp = arr[i]
        it = i
        while it > 0 and comp(arr[it - 1], temp):
            arr[it] = arr[it - 1]
            it -= 1
        arr[it] = temp


if __name__ == '__main__':
    arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
    arr_clone = arr.copy()
    print(f"Array before sort: {arr}")
    insertion_sort(arr, lambda i, j: i > j)
    print(f"Array after ascending sorting: {arr}")
    insertion_sort(arr_clone, lambda i, j: i < j)
    print(f"Array after descending sorting: {arr_clone}")

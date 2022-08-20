from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def insertion_sort(arr: list[int], comp: Callable[[T, T], bool]) -> list[int]:
    if len(arr) == 0:
        raise ValueError("array is empty")
    arr = arr.copy()

    for i in range(1, len(arr)):
        temp = arr[i]
        it = i
        while it > 0 and comp(arr[it - 1], temp):
            arr[it] = arr[it - 1]
            it -= 1
        arr[it] = temp

    return arr


arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
print(f"Array before sort: {arr}")
sortedArray = insertion_sort(arr, lambda i, j: i < j)
print(f"Array after ascending sorting: {sortedArray}")
sortedArray = insertion_sort(arr, lambda i, j: i > j)
print(f"Array after descending sorting: {sortedArray}")

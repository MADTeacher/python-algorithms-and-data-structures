from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def gnome_sort(arr: list[int], comp: Callable[[T, T], bool]) -> list[int]:
    if len(arr) == 0:
        raise ValueError("array is empty")
    arr = arr.copy()

    def swap(i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    i = 1
    while i < len(arr):
        if comp(arr[i], arr[i - 1]):
            i += 1
        else:
            swap(i, i - 1)
            if i > 1:
                i -= 1

    return arr


arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
print(f"Array before sort: {arr}")
sortedArray = gnome_sort(arr, lambda i, j: i < j)
print(f"Array after ascending sorting: {sortedArray}")
sortedArray = gnome_sort(arr, lambda i, j: i > j)
print(f"Array after descending sorting: {sortedArray}")

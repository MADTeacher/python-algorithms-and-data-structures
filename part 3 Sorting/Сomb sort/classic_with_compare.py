from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def comb_sort(arr: list[int], comp: Callable[[T, T], bool]) -> list[int]:
    if len(arr) == 0:
        raise ValueError("array is empty")
    arr = arr.copy()

    def swap(i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    factor = 1.247
    step = len(arr) - 1
    while step >= 1:
        i = 0
        while i + step < len(arr):
            if comp(arr[i], arr[i + int(step)]):
                swap(i, i + int(step))
            i += 1
        step /= factor
    return arr


arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
print(f"Array before sort: {arr}")
sortedArray = comb_sort(arr, lambda i, j: i < j)
print(f"Array after ascending sorting: {sortedArray}")
sortedArray = comb_sort(arr, lambda i, j: i > j)
print(f"Array after descending sorting: {sortedArray}")
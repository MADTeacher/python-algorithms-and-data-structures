from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def partition(arr: list[int], l: int, r: int, comp: Callable[[T, T], bool]) -> int:
    def swap(i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    x = arr[r]
    less = l

    for i in range(l, r):
        if comp(arr[i], x):
            swap(i, less)
            less += 1
    swap(less, r)
    return less


def quick_sort_impl(arr: list[int], l: int, r: int, comp: Callable[[T, T], bool]):
    if l < r:
        q = partition(arr, l, r, comp)
        quick_sort_impl(arr, l, q - 1, comp)
        quick_sort_impl(arr, q + 1, r, comp)


def quick_sort(arr: list[int], comp: Callable[[T, T], bool]) -> list[int]:
    if len(arr) == 0:
        raise ValueError("array is empty")
    arr = arr.copy()
    quick_sort_impl(arr, 0, len(arr) - 1, comp)
    return arr


arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
print(f"Array before sort: {arr}")
sortedArray = quick_sort(arr, lambda i, j: i < j)
print(f"Array after ascending sorting: {sortedArray}")
sortedArray = quick_sort(arr, lambda i, j: i > j)
print(f"Array after descending sorting: {sortedArray}")

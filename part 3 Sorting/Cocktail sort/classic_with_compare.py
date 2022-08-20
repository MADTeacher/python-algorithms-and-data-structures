from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def cocktail_sort(arr: list[int], comp: Callable[[T, T], bool]) -> list[int]:
    if len(arr) == 0:
        raise ValueError("array is empty")
    arr = arr.copy()

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    left = 0
    right = len(arr) - 1

    while left <= right:
        for i in range(right, left, -1):
            if comp(arr[i - 1], arr[i]):
                swap(i - 1, i)
        left += 1
        for i in range(left, right):
            if comp(arr[i], arr[i + 1]):
                swap(i, i + 1)
        right -= 1
    return arr


arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
print(f"Array before sort: {arr}")
sortedArray = cocktail_sort(arr, lambda i, j: i < j)
print(f"Array after ascending sorting: {sortedArray}")
sortedArray = cocktail_sort(arr, lambda i, j: i > j)
print(f"Array after descending sorting: {sortedArray}")

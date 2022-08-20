from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


class Worker:
    def __init__(self, name: str, id: int):
        self.__id = id
        self.__name = name

    def __repr__(self):
        return f"{self.__name}:{self.__id}"

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name


def comb_sort(arr: list[T], comp: Callable[[T, T], bool]) -> list[T]:
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


worker_slice = [Worker(*item) for item in [("Julie", 1), ("Alex", 2), ("Tom", 4),
                                           ("George", 3), ("Max", 60), ("Tommy", 94), ("William", 12),
                                           ("Sophia", 14), ("Oliver", 13), ("Sandra", 91),
                                           ("Ann", 6), ("Elizabeth", 9), ("Kate", 20)]]

print(f"Array before sort: {worker_slice}")
print("---------Sort by id-----------")
sortedArray = comb_sort(worker_slice, lambda i, j: i.get_id() < j.get_id())
print(f"Array after ascending sorting: {sortedArray}")
sortedArray = comb_sort(worker_slice, lambda i, j: i.get_id() > j.get_id())
print(f"Array after descending sorting: {sortedArray}")

print("---------Sort by name-----------")
sortedArray = comb_sort(worker_slice, lambda i, j: i.get_name() < j.get_name())
print(f"Array after ascending sorting: {sortedArray}")
sortedArray = comb_sort(worker_slice, lambda i, j: i.get_name() > j.get_name())
print(f"Array after descending sorting: {sortedArray}")

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


def gnome_sort(array: list, comp: Callable[[T, T], bool]) -> list:
    if len(array) == 0:
        raise ValueError("array is empty")
    arr = array.copy()

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


worker_slice = [Worker(*item) for item in [("Julie", 1), ("Alex", 2), ("Tom", 4),
                                           ("George", 3), ("Max", 60), ("Tommy", 94), ("William", 12),
                                           ("Sophia", 14), ("Oliver", 13), ("Sandra", 91),
                                           ("Ann", 6), ("Elizabeth", 9), ("Kate", 20)]]

print(f"Array before sort: {worker_slice}")
print("---------Sort by id-----------")
sortedArray = gnome_sort(worker_slice, lambda i, j: i.get_id() < j.get_id())
print(f"Array after ascending sorting: {sortedArray}")
sortedArray = gnome_sort(worker_slice, lambda i, j: i.get_id() > j.get_id())
print(f"Array after descending sorting: {sortedArray}")

print("---------Sort by name-----------")
sortedArray = gnome_sort(worker_slice, lambda i, j: i.get_name() < j.get_name())
print(f"Array after ascending sorting: {sortedArray}")
sortedArray = gnome_sort(worker_slice, lambda i, j: i.get_name() > j.get_name())
print(f"Array after descending sorting: {sortedArray}")

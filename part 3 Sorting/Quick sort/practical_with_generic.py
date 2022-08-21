from collections.abc import Callable
import copy
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


def partition(arr: list, l: int, r: int, comp: Callable[[T, T], bool]) -> int:
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


def quick_sort_impl(arr: list[T], l: int, r: int, 
comp: Callable[[T, T], bool]) -> None:
    if l < r:
        q = partition(arr, l, r, comp)
        quick_sort_impl(arr, l, q - 1, comp)
        quick_sort_impl(arr, q + 1, r, comp)


def quick_sort(arr: list[T], comp: Callable[[T, T], bool]) -> None:
    if len(arr) == 0:
        raise ValueError("array is empty")

    quick_sort_impl(arr, 0, len(arr) - 1, comp)


if __name__ == '__main__':
    workers = [Worker(*item) for item in [("Julie", 1),
                                          ("Alex", 2),
                                          ("Tom", 4),
                                          ("George", 3),
                                          ("Max", 60),
                                          ("Tommy", 94),
                                          ("William", 12),
                                          ("Sophia", 14),
                                          ("Oliver", 13),
                                          ("Sandra", 91),
                                          ("Ann", 6),
                                          ("Elizabeth", 9),
                                          ("Kate", 20)]
               ]
    workers_copy = copy.deepcopy(workers)
    print(f"Array before sort: {workers}")

    print("---------Sort by id-----------")
    quick_sort(workers, lambda i, j: i.get_id() < j.get_id())
    print(f"Array after ascending sorting: {workers}")
    quick_sort(workers_copy, lambda i, j: i.get_id() > j.get_id())
    print(f"Array after descending sorting: {workers_copy}")

    print("---------Sort by name-----------")
    quick_sort(workers, lambda i, j: i.get_name() < j.get_name())
    print(f"Array after ascending sorting: {workers}")
    quick_sort(workers_copy, lambda i, j: i.get_name() > j.get_name())
    print(f"Array after descending sorting: {workers_copy}")

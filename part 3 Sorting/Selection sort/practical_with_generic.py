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


def selection_sort(arr: list[T], comp: Callable[[T, T], bool]) -> list[T]:
    if len(arr) == 0:
        raise ValueError("array is empty")

    def swap(i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(0, len(arr)):
        min = i
        for j in range(i, len(arr)):
            if not comp(arr[j], arr[min]):
                min = j
        swap(i, min)


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
    selection_sort(workers, lambda i, j: i.get_id() > j.get_id())
    print(f"Array after ascending sorting: {workers}")
    selection_sort(workers_copy, lambda i, j: i.get_id() < j.get_id())
    print(f"Array after descending sorting: {workers_copy}")

    print("---------Sort by name-----------")
    selection_sort(workers, lambda i, j: i.get_name() > j.get_name())
    print(f"Array after ascending sorting: {workers}")
    selection_sort(workers_copy, lambda i, j: i.get_name() < j.get_name())
    print(f"Array after descending sorting: {workers_copy}")
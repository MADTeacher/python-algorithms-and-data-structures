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


def cocktail_sort(arr: list[T], comp: Callable[[T, T], bool]) -> None:
    if len(arr) == 0:
        raise ValueError("array is empty")

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
    cocktail_sort(workers, lambda i, j: i.get_id() > j.get_id())
    print(f"Array after ascending sorting: {workers}")
    cocktail_sort(workers_copy, lambda i, j: i.get_id() < j.get_id())
    print(f"Array after descending sorting: {workers_copy}")

    print("---------Sort by name-----------")
    cocktail_sort(workers, lambda i, j: i.get_name() > j.get_name())
    print(f"Array after ascending sorting: {workers}")
    cocktail_sort(workers_copy, lambda i, j: i.get_name() < j.get_name())
    print(f"Array after descending sorting: {workers_copy}")

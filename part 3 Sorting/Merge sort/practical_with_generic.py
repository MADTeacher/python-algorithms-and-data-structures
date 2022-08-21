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


def merge_sort_impl(arr: list[T], buffer: list[T], l: int,
                    r: int, comp: Callable[[T, T], bool]) -> None:
    if l < r:
        m = (l + r) // 2
        merge_sort_impl(arr, buffer, l, m, comp)
        merge_sort_impl(arr, buffer, m + 1, r, comp)

        k, j = l, m + 1
        i = l
        while i <= m or j <= r:
            if j > r or (i <= m and comp(arr[i], arr[j])):
                buffer[k] = arr[i]
                i += 1
            else:
                buffer[k] = arr[j]
                j += 1
            k += 1

        for i in range(l, r + 1):
            arr[i] = buffer[i]


def merge_sort(arr: list[T], comp: Callable[[T, T], bool]) -> None:
    if len(arr) == 0:
        raise ValueError("array is empty")

    buffer = [None for _ in range(len(arr))]
    merge_sort_impl(arr, buffer, 0, len(arr) - 1, comp)


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
    merge_sort(workers, lambda i, j: i.get_id() < j.get_id())
    print(f"Array after ascending sorting: {workers}")
    merge_sort(workers_copy, lambda i, j: i.get_id() > j.get_id())
    print(f"Array after descending sorting: {workers_copy}")

    print("---------Sort by name-----------")
    merge_sort(workers, lambda i, j: i.get_name() < j.get_name())
    print(f"Array after ascending sorting: {workers}")
    merge_sort(workers_copy, lambda i, j: i.get_name() > j.get_name())
    print(f"Array after descending sorting: {workers_copy}")

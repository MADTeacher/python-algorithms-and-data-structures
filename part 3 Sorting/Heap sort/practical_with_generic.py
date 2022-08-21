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


class Heap:
    def __init__(self, values: list[T], comp: Callable[[T, T], bool]):
        self.__length: int = 0
        self.__comp: Callable[[T, T], bool] = comp
        self.__arr: list[T] = []
        for it in values:
            self.insert(it)

    def trickle_up(self, index: int) -> None:
        parent: int = (index - 1) // 2
        bottom: T = self.__arr[index]

        while index > 0 and self.__comp(self.__arr[parent], bottom):
            self.__arr[index] = self.__arr[parent]
            index = parent
            parent = (parent - 1) // 2

        self.__arr[index] = bottom

    def trickle_down(self, index: int) -> None:
        large_child: int
        top: T = self.__arr[index]
        while index < self.__length // 2:
            left_child: int = 2 * index + 1
            right_child: int = left_child + 1
            if (right_child < self.__length and
                    self.__comp(self.__arr[left_child], self.__arr[right_child])):
                large_child = right_child
            else:
                large_child = left_child

            if not self.__comp(top, self.__arr[large_child]):
                break

            # Потомок сдвигается вверх
            self.__arr[index] = self.__arr[large_child]
            index = large_child

        self.__arr[index] = top  # index <- корень

    def insert(self, value: T) -> None:
        self.__arr.append(value)
        self.trickle_up(self.__length)
        self.__length += 1

    def remove(self) -> T:
        if len(self.__arr) == 0:
            raise ValueError("array is empty")

        root: T = self.__arr[0]
        self.__length -= 1
        self.__arr[0] = self.__arr[self.__length]
        self.trickle_down(0)
        return root

def heap_sort(arr: list[T], comp: Callable[[T, T], bool]) -> None:
    if len(arr) == 0:
        raise ValueError("array is empty")

    heap = Heap(arr, comp)
    for i in range(len(arr) - 1, -1, -1):
        arr[i] = heap.remove()


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
    heap_sort(workers, lambda i, j: i.get_id() < j.get_id())
    print(f"Array after ascending sorting: {workers}")
    heap_sort(workers_copy, lambda i, j: i.get_id() > j.get_id())
    print(f"Array after descending sorting: {workers_copy}")

    print("---------Sort by name-----------")
    heap_sort(workers, lambda i, j: i.get_name() < j.get_name())
    print(f"Array after ascending sorting: {workers}")
    heap_sort(workers_copy, lambda i, j: i.get_name() > j.get_name())
    print(f"Array after descending sorting: {workers_copy}")

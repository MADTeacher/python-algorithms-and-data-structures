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


def get_min(a: int, b: int) -> int:
    if a <= b:
        return a
    else:
        return b


def fibonacci_search(arr: list[Worker], x: int) -> int:
    if x < arr[0].get_id() or x > arr[len(arr) - 1].get_id():
        raise ValueError("Not Found")

    fm2 = 0
    fm1 = 1
    fm = fm1 + fm2
    offset = -1

    while fm < len(arr):
        fm2 = fm1
        fm1 = fm
        fm = fm1 + fm2

    while fm > 1:
        i = get_min(offset + fm2, len(arr) - 1)
        if arr[i].get_id() < x:
            fm = fm1
            fm1 = fm2
            fm2 = fm - fm1
            offset = i
        elif arr[i].get_id() > x:
            fm = fm2
            fm1 = fm1 - fm2
            fm2 = fm - fm1
        else:
            return i

    if fm1 == 1:
        if arr[offset + 1].get_id() == x:
            return offset + 1

    raise ValueError("Not Found")


worker_slice = [Worker(*item) for item in [("Julie", 1), ("Alex", 2), ("Tom", 4),
                                           ("George", 3), ("Max", 60), ("Tommy", 94), ("William", 12),
                                           ("Sophia", 14), ("Oliver", 13), ("Sandra", 91),
                                           ("Ann", 6), ("Elizabeth", 9), ("Kate", 20)]]

# сортировка по возрастанию id
worker_slice.sort(key=lambda el: el.get_id())
print(f"Array after sorting by id: {worker_slice}")

# поиск по существующему id
id = 4
index = fibonacci_search(worker_slice, id)
print(f"Element is located by the index: {index}, its value: {worker_slice[index]}")

# поиск по не существующему id
id = 32
try:
    index = fibonacci_search(worker_slice, id)
except ValueError as e:
    print(f"Searching {id} : {e}")

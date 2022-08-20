import math
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


# ------------------- Поиск по id -------------------
def jump_search_by_id(arr: list[Worker], x: int) -> int:
    if x < arr[0].get_id() or x > arr[len(arr) - 1].get_id():
        raise ValueError("Not Found")

    if x < arr[0].get_id() or x > arr[len(arr) - 1].get_id():
        raise ValueError("Not Found")

    step, pos = 0, 0
    step = math.floor(len(arr) ** 0.5)
    while arr[pos].get_id() < x:
        if arr[step].get_id() > x or step >= len(arr):
            break
        else:
            pos = step
            step += math.floor(len(arr) ** 0.5)

    while arr[pos].get_id() < x:
        pos += 1

    if arr[pos].get_id() == x:
        return pos

    raise ValueError("Not Found")


# -------------------  Поиск по name -------------------
def jump_search_by_name(arr: list[Worker], x: str) -> int:
    if x < arr[0].get_name() or x > arr[len(arr) - 1].get_name():
        raise ValueError("Not Found")

    if x < arr[0].get_name() or x > arr[len(arr) - 1].get_name():
        raise ValueError("Not Found")

    step, pos = 0, 0
    step = math.floor(len(arr) ** 0.5)
    while arr[pos].get_name() < x:
        if arr[step].get_name() > x or step >= len(arr):
            break
        else:
            pos = step
            step += math.floor(len(arr) ** 0.5)

    while arr[pos].get_name() < x:
        pos += 1

    if arr[pos].get_name() == x:
        return pos

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
index = jump_search_by_id(worker_slice, id)
print(f"Element is located by the index: {index}, its value: {worker_slice[index]}")

# поиск по не существующему id
id = 32
try:
    index = jump_search_by_id(worker_slice, id)
except ValueError as e:
    print(f"Searching {id} : {e}")

# сортировка по возрастанию name
worker_slice.sort(key=lambda el: el.get_name())
print(f"Array after sorting by name: {worker_slice}")

# поиск по существующему name
name = "Kate"
index = jump_search_by_name(worker_slice, name)
print(f"Element is located by the index: {index}, its value: {worker_slice[index]}")

# поиск по не существующему name
name = "Timmy"
try:
    index = jump_search_by_name(worker_slice, name)
except ValueError as e:
    print(f"Searching {name} : {e}")

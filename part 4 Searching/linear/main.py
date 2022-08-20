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
def linear_search_by_id(arr: list[Worker], id: int) -> int:
    for i, val in enumerate(arr):
        if id == val.get_id():
            return i
        if id < val.get_id():
            break
    raise ValueError("Not Found")


# -------------------  Поиск по name -------------------
def linear_search_by_name(arr: list[Worker], name: str) -> int:
    for i, val in enumerate(arr):
        if name == val.get_name():
            return i
        if name < val.get_name():
            break
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
index = linear_search_by_id(worker_slice, id)
print(f"Element is located by the index: {index}, its value: {worker_slice[index]}")

# поиск по не существующему id
id = 32
try:
    index = linear_search_by_id(worker_slice, id)
except ValueError as e:
    print(f"Searching {id} : {e}")

# сортировка по возрастанию name
worker_slice.sort(key=lambda el: el.get_name())
print(f"Array after sorting by name: {worker_slice}")

# поиск по существующему name
name = "Kate"
index = linear_search_by_name(worker_slice, name)
print(f"Element is located by the index: {index}, its value: {worker_slice[index]}")

# поиск по не существующему name
name = "Timmy"
try:
    index = linear_search_by_name(worker_slice, name)
except ValueError as e:
    print(f"Searching {name} : {e}")

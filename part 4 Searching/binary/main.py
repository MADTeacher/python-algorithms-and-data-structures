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
def binary_search_by_id_impl(arr: list[Worker], target_id: int, l: int, r: int) -> int:
    if r < l or len(arr) == 0:
        raise ValueError("Not Found")

    mid = l + (r - l) // 2
    if arr[mid].get_id() > target_id:
        return binary_search_by_id_impl(arr, target_id, l, mid - 1)
    elif arr[mid].get_id() < target_id:
        return binary_search_by_id_impl(arr, target_id, mid + 1, r)
    else:
        return mid


def binary_search_by_id(arr: list[Worker], id: int) -> int:
    if id < arr[0].get_id() or id > arr[len(arr) - 1].get_id():
        raise ValueError("Not Found")

    return binary_search_by_id_impl(arr, id, 0, len(arr) - 1)


# -------------------  Поиск по name -------------------
def binary_search_by_name_impl(arr: list[Worker], target_name: str, l: int, r: int) -> int:
    if r < l or len(arr) == 0:
        raise ValueError("Not Found")

    mid = l + (r - l) // 2
    if arr[mid].get_name() > target_name:
        return binary_search_by_name_impl(arr, target_name, l, mid - 1)
    elif arr[mid].get_name() < target_name:
        return binary_search_by_name_impl(arr, target_name, mid + 1, r)
    else:
        return mid


def binary_search_by_name(arr: list[Worker], name: str) -> int:
    if name < arr[0].get_name() or name > arr[len(arr) - 1].get_name():
        raise ValueError("Not Found")

    return binary_search_by_name_impl(arr, name, 0, len(arr) - 1)


worker_slice = [Worker(*item) for item in [("Julie", 1), ("Alex", 2), ("Tom", 4),
                                           ("George", 3), ("Max", 60), ("Tommy", 94), ("William", 12),
                                           ("Sophia", 14), ("Oliver", 13), ("Sandra", 91),
                                           ("Ann", 6), ("Elizabeth", 9), ("Kate", 20)]]

# сортировка по возрастанию id
worker_slice.sort(key=lambda el: el.get_id())
print(f"Array after sorting by id: {worker_slice}")

# поиск по существующему id
id = 4
index = binary_search_by_id(worker_slice, id)
print(f"Element is located by the index: {index}, its value: {worker_slice[index]}")

# поиск по не существующему id
id = 32
try:
    index = binary_search_by_id(worker_slice, id)
except ValueError as e:
    print(f"Searching {id} : {e}")

# сортировка по возрастанию имени
worker_slice.sort(key=lambda el: el.get_name())
print(f"Array after sorting by Name: {worker_slice}")

# поиск по name
name = "Kate"
index = binary_search_by_name(worker_slice, name)
print(f"Element is located by the index: {index}, its value: {worker_slice[index]}")

# поиск по не существующему name
name = "Timmy"
try:
    index = binary_search_by_name(worker_slice, name)
except ValueError as e:
    print(f"Searching {name} : {e}")

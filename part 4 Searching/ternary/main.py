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
def ternary_search_by_id_impl(arr: list[Worker], target_id: int, l: int, r: int) -> int:
    if r > l:
        if r - l == 1:
            if target_id == arr[r].get_id():
                return r

            if target_id == arr[l].get_id():
                return l

            raise ValueError("Not Found")

        step = round((r-l) / 3)
        m1 = l + step
        m2 = m1 + step
        if target_id == arr[m1].get_id():
            return m1

        if target_id == arr[m2].get_id():
            return m2

        if target_id < arr[m1].get_id():
            return ternary_search_by_id_impl(arr, target_id, l, m1)
        elif arr[m1].get_id() < target_id < arr[m2].get_id():
            return ternary_search_by_id_impl(arr, target_id, m1, m2)
        else:
            return ternary_search_by_id_impl(arr, target_id, m2, r)

    raise ValueError("Not Found")


def ternary_search_by_id(arr: list[Worker], id: int) -> int:
    if id < arr[0].get_id() or id > arr[len(arr) - 1].get_id():
        raise ValueError("Not Found")

    return ternary_search_by_id_impl(arr, id, 0, len(arr) - 1)


# -------------------  Поиск по name -------------------
def ternary_search_by_name_impl(arr: list[Worker], target_name: str, l: int, r: int) -> int:
    if r > l:
        if r - l == 1:
            if target_name == arr[r].get_name():
                return r

            if target_name == arr[l].get_name():
                return l

            raise ValueError("Not Found")

        step = round((r-l) / 3)
        m1 = l + step
        m2 = m1 + step
        if target_name == arr[m1].get_name():
            return m1

        if target_name == arr[m2].get_name():
            return m2

        if target_name < arr[m1].get_name():
            return ternary_search_by_name_impl(arr, target_name, l, m1)
        elif arr[m1].get_name() < target_name < arr[m2].get_name():
            return ternary_search_by_name_impl(arr, target_name, m1, m2)
        else:
            return ternary_search_by_name_impl(arr, target_name, m2, r)

    raise ValueError("Not Found")


def ternary_search_by_name(arr: list[Worker], id: str) -> int:
    if id < arr[0].get_name() or id > arr[len(arr) - 1].get_name():
        raise ValueError("Not Found")

    return ternary_search_by_name_impl(arr, id, 0, len(arr) - 1)


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
    # сортировка по возрастанию id
    workers.sort(key=lambda el: el.get_id())
    print(f"Array after sorting by id: {workers}")

    # поиск по существующему id
    id = 4
    index = ternary_search_by_id(workers, id)
    print(f"Element is located by the index: {index}, its value: {workers[index]}")

    # поиск по не существующему id
    id = 32
    try:
        index = ternary_search_by_id(workers, id)
    except ValueError as e:
        print(f"Searching {id} : {e}")

    # сортировка по возрастанию name
    workers.sort(key=lambda el: el.get_name())
    print(f"Array after sorting by name: {workers}")

    # поиск по существующему name
    name = "Kate"
    index = ternary_search_by_name(workers, name)
    print(f"Element is located by the index: {index}, its value: {workers[index]}")

    # поиск по не существующему name
    name = "Timmy"
    try:
        index = ternary_search_by_name(workers, name)
    except ValueError as e:
        print(f"Searching {name} : {e}")

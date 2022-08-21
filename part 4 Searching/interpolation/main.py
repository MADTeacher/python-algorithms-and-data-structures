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


def interpolation_search(arr: list[Worker], x: int) -> int:
    if x < arr[0].get_id() or x > arr[len(arr) - 1].get_id():
        raise ValueError("Not Found")

    high = len(arr) - 1
    low = 0
    while (arr[high].get_id() != arr[low].get_id() and
           arr[low].get_id() <= x <= arr[high].get_id()):
        pos = low + int((high - low) /
                        (arr[high].get_id() - arr[low].get_id()) *
                        (x - arr[low].get_id()))
        if arr[pos].get_id() == x:
            return pos
        elif arr[pos].get_id() < x:
            low = pos + 1
        else:
            high = pos - 1

    raise ValueError("Not Found")


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
    index = interpolation_search(workers, id)
    print(
        f"Element is located by the index: {index}, its value: {workers[index]}")

    # поиск по не существующему id
    id = 32
    try:
        index = interpolation_search(workers, id)
    except ValueError as e:
        print(f"Searching {id} : {e}")

from typing import TypeVar, Generic, Optional, Callable

T = TypeVar("T", int, str)

MySetType = dict[T, None]


class MySet(Generic[T]):

    def __init__(self, *arg) -> None:
        self._set: MySetType = {}
        if len(arg) == 0:
            return
        for it in list(arg):
            self.add(it)

    def add(self, value: T) -> bool:
        length = len(self._set)
        self._set[value] = None
        return length != len(self._set)

    def is_empty(self) -> bool:
        return len(self._set) == 0

    def size(self) -> int:
        return len(self._set)

    def remove_all(self) -> None:
        self._set: MySetType = {}

    def contains(self, value: T) -> bool:
        return value in self._set

    def difference(self, other: 'MySet[T]') -> 'MySet[T]':
        new_set: MySet[T] = MySet()
        for k in self._set.keys():
            if not other.contains(k):
                new_set.add(k)

        return new_set

    def symmetric_difference(self, other: 'MySet[T]') -> 'MySet[T]':
        new_set: MySet[T] = MySet()
        for k in self._set.keys():
            if not other.contains(k):
                new_set.add(k)
        for k in other._set.keys():
            if not self.contains(k):
                new_set.add(k)
        return new_set

    def intersect(self, other: 'MySet[T]') -> 'MySet[T]':
        new_set: MySet[T] = MySet()
        if self.size() < other.size():
            for k in self._set.keys():
                if other.contains(k):
                    new_set.add(k)
        else:
            for k in other._set.keys():
                if self.contains(k):
                    new_set.add(k)
        return new_set

    def union(self, other: 'MySet[T]') -> 'MySet[T]':
        new_set: MySet[T] = MySet()
        for k in self._set.keys():
            new_set.add(k)
        for k in other._set.keys():
            new_set.add(k)
        return new_set

    def is_subset(self, other: 'MySet[T]') -> bool:
        if self.size() < other.size():
            return False
        for k in self._set.keys():
            if not other.contains(k):
                return False
        return True

    def for_each(self, func: Callable[[T], None]) -> None:
        if self.size() == 0:
            return
        for k in self._set.keys():
            func(k)

    def print_set(self) -> None:
        print(list(self._set.keys()))


if __name__ == '__main__':
    set_a = MySet(1, 2, 3, 4, 5, 6, 3, 3, 3, 2, 1, 4, 7, 8, 5)
    print("----- setA ------")
    set_a.print_set()

    set_b = MySet(10, 22, 1, 4, 21, 4, 5, 21, 11, 10)
    print("----- setB ------")
    set_b.print_set()

    print("----- Contains ------")
    val = 10
    print(f"SetA is contains '{val}'? {set_a.contains(val)}")
    print(f"SetB is contains '{val}'? {set_b.contains(val)}")

    print("-----  A - B  ------")
    set_a.difference(set_b).print_set()
    print("----- B - A ------")
    set_b.difference(set_a).print_set()
    print("----- Symmetric Difference ------")
    set_a.symmetric_difference(set_b).print_set()
    print("----- Union  ------")
    set_a.union(set_b).print_set()
    print("----- Intersect  ------")
    set_a.intersect(set_b).print_set()
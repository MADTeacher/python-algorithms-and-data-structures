import ctypes
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar("T")


class IndexOutRangeException(Exception):
    pass


@dataclass
class Cat:
    name: str
    age: int

    def __str__(self) -> str:
        return f"Cat({self.name},{self.age})"


class DynamicArray(Generic[T]):

    def __init__(self, capacity: int) -> None:
        self._length: int = 0
        self._capacity: int = capacity
        self._arr: ctypes.Array[T] = (capacity * ctypes.py_object)()

    def get_length(self) -> int:
        return self._length

    def get_capacity(self) -> int:
        return self._capacity

    def _resize(self, new_capacity: int) -> None:
        new_array: ctypes.Array[T] = (new_capacity * ctypes.py_object)()
        for it in range(self._length):
            new_array[it] = self._arr[it]

        self._arr = new_array
        self._capacity = new_capacity
        print(f"New capacity = {new_capacity}")

    def _check_range(self, index: int) -> bool:
        if index >= self._length or index < 0:
            return False
        return True

    def is_empy(self) -> bool:
        return self._length == 0

    def add(self, element: T) -> None:
        if self._length == self._capacity:
            self._resize(self._capacity * 2)

        self._arr[self._length] = element
        self._length += 1
        print(self)

    def get(self, index: int) -> T:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")

        return self._arr[index]

    def remove(self, index: int) -> bool:
        ok: bool = self._check_range(index)
        if not ok:
            return False

        for i in range(index, self._length-1):
            self._arr[i] = self._arr[i + 1]
        self._length -= 1
        return ok

    def put(self, index: int, element: T) -> bool:
        ok: bool = self._check_range(index)
        if not ok:
            return False

        self._arr[index] = element
        return ok

    def __str__(self) -> str:
        my_str: str = ""
        for it in range(self._length):
            my_str += str(self._arr[it]) + " "
        return f"Current state: [{my_str}]"


if __name__ == '__main__':
    dynamic_array = DynamicArray[Cat](capacity=10)
    print(dynamic_array)
    dynamic_array.add(Cat("Max", 4))
    dynamic_array.add(Cat("Alex", 5))
    dynamic_array.add(Cat("Tom", 7))
    dynamic_array.remove(0)
    print(dynamic_array)
    dynamic_array.put(1, Cat("Tommy", 1))
    print(dynamic_array)

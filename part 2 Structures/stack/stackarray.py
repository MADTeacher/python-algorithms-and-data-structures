import ctypes
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar("T")


class StackOverFlowException(Exception):
    pass


class EmptyStackException(Exception):
    pass


@dataclass
class Cat:
    name: str
    age: int

    def __str__(self) -> str:
        return f"Cat({self.name},{self.age})"


class StackArray(Generic[T]):

    def __init__(self, size: int) -> None:
        self._length: int = 0
        self.fixed_size: int = size
        self._arr: ctypes.Array[T] = (size * ctypes.py_object)()

    def get_size(self) -> int:
        return self._length

    def is_empty(self) -> bool:
        return self._length == 0

    def push(self, value: T):
        if self._length >= self.fixed_size:
            raise StackOverFlowException(f"StackOverFlowException: {value}")
        self._arr[self._length] = value
        self._length += 1

    def pop(self) -> T:
        if self.is_empty():
            raise EmptyStackException("StackOverFlowException")
        old_length = self._length - 1
        self._length -= 1
        return self._arr[old_length]

    def peak(self) -> T:
        if self.is_empty():
            raise EmptyStackException("Stack is empty")
        return self._arr[self._length - 1]

    def print_stack(self) -> None:
        if self.is_empty():
            print("Stack is empty")
        my_list: list[T] = []
        for it in range(self._length-1, -1, -1):
            my_list.append(self._arr[it])
        print(f"Stack: {my_list}")


if __name__ == '__main__':
    fix_size: int = 3
    stack: StackArray[Cat] = StackArray[Cat](fix_size)
    try:
        stack.push(Cat("Max", 4))
        stack.push(Cat("Alex", 5))
        stack.push(Cat("Tom", 7))
        stack.print_stack()
        stack.push(Cat("Tommy", 1))
    except StackOverFlowException as ex:
        print(ex)

    print(f"Stack head value: {stack.peak()}")

    print("----- Pop ------")
    try:
        for i in range(0, fix_size + 1):
            pop_value = stack.pop()
            print(f"Stack head value: {pop_value}")

    except EmptyStackException as ex:
        print(ex)
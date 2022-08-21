import ctypes
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar("T")


class QueueOverFlowException(Exception):
    pass


class EmptyQueueException(Exception):
    pass


@dataclass
class Cat:
    name: str
    age: int

    def __str__(self) -> str:
        return f"Cat({self.name},{self.age})"


class QueueArray(Generic[T]):

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
            raise QueueOverFlowException(f"QueueOverFlowException: {value}")
        self._arr[self._length] = value
        self._length += 1

    def pop(self) -> T:
        if self.is_empty():
            raise EmptyQueueException("EmptyQueueException")
        data = self._arr[0]
        for it in range(1, self._length):
            self._arr[it - 1] = self._arr[it]
        self._length -= 1
        return data

    def peak(self) -> T:
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        return self._arr[0]

    def print_stack(self) -> None:
        if self.is_empty():
            print("Queue is empty")
        my_list: list[T] = []
        for it in range(0, self._length):
            my_list.append(self._arr[it])
        print(f"Queue: {my_list}")


if __name__ == '__main__':
    fix_size: int = 3
    queue: QueueArray[Cat] = QueueArray[Cat](fix_size)
    try:
        queue.push(Cat("Max", 4))
        queue.push(Cat("Alex", 5))
        queue.push(Cat("Tom", 7))
        queue.print_stack()
        queue.push(Cat("Tommy", 1))
    except QueueOverFlowException as ex:
        print(ex)

    print(f"Queue head value: {queue.peak()}")

    print("----- Pop ------")
    try:
        for i in range(0, fix_size + 1):
            pop_value = queue.pop()
            print(f"Queue head value: {pop_value}")

    except EmptyQueueException as ex:
        print(ex)
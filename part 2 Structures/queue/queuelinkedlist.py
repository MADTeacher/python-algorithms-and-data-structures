from dataclasses import dataclass
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class EmptyQueueException(Exception):
    pass


@dataclass
class Cat:
    name: str
    age: int

    def __str__(self) -> str:
        return f"Cat({self.name},{self.age})"


@dataclass
class SingleNode(Generic[T]):
    data: T
    next_ptr: Optional['SingleNode[T]'] = None


class QueueLinkedList(Generic[T]):

    def __init__(self) -> None:
        self._length: int = 0
        self._head: Optional[SingleNode[T]] = None
        self._tail: Optional[SingleNode[T]] = None

    def get_size(self) -> int:
        return self._length

    def is_empty(self) -> bool:
        return self._length == 0

    def push(self, value: T):
        node = SingleNode[T](value, None)
        if self._length == 0:
            self._head = node
            self._tail = node
            self._length += 1
            return

        self._tail.next_ptr = node
        self._tail = node
        self._length += 1

    def pop(self) -> T:
        if self.is_empty():
            raise EmptyQueueException("EmptyQueueException")
        node = self._head
        self._head = node.next_ptr
        self._length -= 1
        return node.data

    def peak(self) -> T:
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        return self._head.data

    def print_queue(self) -> None:
        if self.is_empty():
            print("Stack is empty")
        my_list: list[T] = []
        current_node = self._head
        my_list.append(current_node.data)
        while current_node.next_ptr is not None:
            current_node = current_node.next_ptr
            my_list.append(current_node.data)
        print(f"Queue: {my_list}")


if __name__ == '__main__':
    queue: QueueLinkedList[Cat] = QueueLinkedList[Cat]()
    queue.push(Cat("Max", 4))
    queue.push(Cat("Alex", 5))
    queue.push(Cat("Tom", 7))
    queue.push(Cat("Tommy", 1))
    queue.print_queue()

    print(f"Queue head value: {queue.peak()}")

    print("----- Pop ------")
    length = queue.get_size()
    try:
        for i in range(0, length + 1):
            pop_value = queue.pop()
            print(f"Queue head value: {pop_value}")

    except EmptyQueueException as ex:
        print(ex)

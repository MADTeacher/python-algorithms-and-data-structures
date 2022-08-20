from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable

T = TypeVar("T")


class IndexOutRangeException(Exception):
    pass


@dataclass
class Cat:
    name: str
    age: int

    def __str__(self) -> str:
        return f"Cat({self.name},{self.age})"


@dataclass
class CyclicNode(Generic[T]):
    data: T
    next_ptr: Optional['CyclicNode[T]'] = None
    prev_ptr: Optional['CyclicNode[T]'] = None


class CyclicLinkedList(Generic[T]):

    def __init__(self) -> None:
        self._length: int = 0
        self._head: Optional[CyclicNode[T]] = None

    def get_size(self) -> int:
        return self._length

    def _check_range(self, index: int) -> bool:
        if index >= self._length or index < 0:
            return False
        return True

    def is_empy(self) -> bool:
        return self._length == 0

    def add(self, data: T) -> None:
        node = CyclicNode[T](data, None)
        if self.is_empy():
            node.prev_ptr = node
            node.next_ptr = node
            self._head = node
        else:
            node.prev_ptr = self._head.prev_ptr
            node.next_ptr = self._head
            self._head.prev_ptr.next_ptr = node
            self._head.prev_ptr = node
            self._head = node
        self._length += 1

    def for_each(self, func: Callable[[T], None]) -> None:
        node = self._head
        func(node.data)
        for i in range(0, self._length - 1):
            node = node.next_ptr
            func(node.data)

    def reverse_for_each(self, func: Callable[[T], None]) -> None:
        node = self._head
        func(node.data)
        for i in range(0, self._length - 1):
            node = node.prev_ptr
            func(node.data)

    def rotate(self, delta: int) -> None:
        # изменение элемента на которую указывает вершина
        # зависит от знака аргумента delta
        # не может выходить за длину списка
        if self._length > 0:
            if delta < 0:
                scaling_coef = self._length - 1 - delta // self._length
                delta += scaling_coef * self._length
            delta %= self._length

            if delta > self._length / 2:
                delta = self._length - delta
                for i in range(0, delta):
                    self._head = self._head.prev_ptr
            elif delta == 0:
                return
            else:
                for i in range(0, delta):
                    self._head = self._head.next_ptr

    def value(self) -> Optional[T]:
        if self.is_empy():
            return None
        return self._head.data

    def remove(self) -> bool:
        if self.is_empy():
            return False

        current_node = self._head
        next_node = current_node.next_ptr
        prev_node = current_node.prev_ptr

        if self._length == 1:
            self._head = None
        else:
            self._head = next_node
            next_node.prev_ptr = prev_node
            prev_node.next_ptr = next_node
        self._length -= 1
        return True

    def remove_all(self):
        while self.remove():
            ...

    def __str__(self) -> str:
        my_str: str = ""
        if not self.is_empy():
            node = self._head
            my_str += str(node.data) + " "
            for i in range(0, self._length - 1):
                node = node.next_ptr
                my_str += str(node.data) + " "
        return f"Current state: [{my_str}]"


def print_list(data: T):
    print(data)


if __name__ == '__main__':
    cyclic_linked_list = CyclicLinkedList[Cat]()
    print(cyclic_linked_list)
    cyclic_linked_list.add(Cat("Max", 4))
    cyclic_linked_list.add(Cat("Alex", 5))
    cyclic_linked_list.add(Cat("Tom", 7))
    cyclic_linked_list.add(Cat("Tommy", 1))
    print(f"List size: {cyclic_linked_list.get_size()}")
    cyclic_linked_list.for_each(print_list)
    print("--Remove data--")
    cyclic_linked_list.remove()
    print(cyclic_linked_list)
    print("--Rotate--")
    print(f"Head data before rotate: {cyclic_linked_list.value()}")
    cyclic_linked_list.rotate(-1)
    print(f"Head data before rotate: {cyclic_linked_list.value()}")
    print("--ReverseForEach--")
    cyclic_linked_list.reverse_for_each(print_list)


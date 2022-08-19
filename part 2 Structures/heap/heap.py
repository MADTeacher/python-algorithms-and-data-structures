import ctypes
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable

T = TypeVar("T")


class IKey(ABC):

    @abstractmethod
    def key(self) -> int:
        ...


class HeapOverFlowException(Exception):
    pass


class EmptyHeapException(Exception):
    pass


class IndexOutRangeException(Exception):
    pass


@dataclass
class Cat(IKey):
    name: str
    age: int

    def key(self) -> int:
        return self.age

    def __str__(self) -> str:
        return f"Cat({self.name},{self.age})"


class Heap(Generic[T]):

    def __init__(self, size: int,
                 fixed: bool = False,
                 comp: Callable[[T, T], bool] = lambda a, b: a.key() < b.key()) -> None:
        self._length: int = 0
        self._capacity: int = size
        self._is_fixed: bool = fixed
        self._comp: Callable[[T, T], bool] = comp
        self._arr: ctypes.Array[Optional[T]] = (size * ctypes.py_object)()
        for i in range(0, size):
            self._arr[i] = None

    @staticmethod
    def create_heap_from_list(data: list[T],
                              fixed: bool = True,
                              comp: Callable[[T, T], bool] = lambda a, b: a.key() < b.key()) -> 'Heap[T]':
        heap: Heap[T] = Heap[T](size=len(data), fixed=fixed, comp=comp)
        for it in data:
            heap.insert(it)

        return heap

    def _check_range(self, index: int) -> bool:
        if index >= self._length or index < 0:
            return False
        return True

    def _resize(self, new_capacity: int) -> None:
        new_array: ctypes.Array[T] = (new_capacity * ctypes.py_object)()
        for it in range(self._length):
            new_array[it] = self._arr[it]

        self._arr = new_array
        self._capacity = new_capacity
        print(f"New capacity = {new_capacity}")

    def is_empty(self) -> bool:
        return self._length == 0

    def get_size(self) -> int:
        return self._length

    def trickle_up(self, index: int) -> None:
        parent: int = (index - 1) // 2
        bottom: T = self._arr[index]

        while index > 0 and self._comp(self._arr[parent], bottom):
            self._arr[index] = self._arr[parent]
            index = parent
            parent = (parent - 1) // 2

        self._arr[index] = bottom

    def trickle_down(self, index: int) -> None:
        large_child: int = 0
        top: T = self._arr[index]
        while index < self._length // 2:
            left_child: int = 2 * index + 1
            right_child: int = left_child + 1
            if (right_child < self._length and
                    self._comp(self._arr[large_child], self._arr[right_child])):
                large_child = right_child
            else:
                large_child = left_child

            if not self._comp(top, self._arr[large_child]):
                break

            # Потомок сдвигается вверх
            self._arr[index] = self._arr[large_child]
            index = large_child

        self._arr[index] = top  # index <- корень

    def change(self, index: int, new_value: T) -> None:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("IndexOutRangeException")

        old_value: T = self._arr[index]
        self._arr[index] = new_value
        if self._comp(old_value, new_value):
            self.trickle_up(index)
        else:
            self.trickle_down(index)

    def insert(self, value: T) -> None:
        if self._length >= self._capacity:
            if self._is_fixed:
                raise HeapOverFlowException(f"StackOverFlowException: {value}")
            else:
                self._resize(self._capacity*2)

        self._arr[self._length] = value
        self.trickle_up(self._length)
        self._length += 1

    def remove(self) -> T:
        if self.is_empty():
            raise EmptyHeapException("EmptyHeapException")

        root: T = self._arr[0]
        self._length -= 1
        self._arr[0] = self._arr[self._length]
        self.trickle_down(0)
        return root

    def print_heap(self) -> None:
        print("heapArray: ")
        for it in range(0, self._length):
            if self._arr[it] is not None:
                print(f"{self._arr[it].key()} ", end='')
            else:
                print("-- ", end='')

        print("")

        n_blanks, items_per_row, column, j = (32, 1, 0, 0)
        dots: str = 32 * "."
        print(dots * 2)
        while self._length > 0:
            if column == 0:
                for it in range(0, n_blanks):
                    print(" ", end='')

            print(f"{self._arr[j].key()} ", end='')
            j += 1
            if j >= self._length:
                break

            column += 1
            if column == items_per_row:
                # Конец строки
                n_blanks //= 2  # Половина пробелов
                items_per_row *= 2  # Вдвое больше элементов
                column = 0  # Начать заново
                print("")  # Переход на новую строку
            else:
                for it in range(0, n_blanks * 2 - 2):
                    print(" ", end='')
        print("\n" + dots * 2)


if __name__ == '__main__':
    cats: list[Cat] = [Cat("Max", 4), Cat("Alex", 5), Cat("Tom", 7),
                       Cat("Tommy", 1), Cat("Max", 14), Cat("Alex", 53),
                       Cat("Tom", 79), Cat("Tommy", 11), Cat("Max", 43),
                       Cat("Alex", 5), Cat("Tom", 17), Cat("Tommy", 31),
                       ]
    heap: Heap[Cat] = Heap[Cat].create_heap_from_list(cats)

    heap.print_heap()
    print("----- Remove ------")
    print(f"Remove root: {heap.remove()}")
    heap.print_heap()
    print("----- Change ------")
    heap.change(3, Cat("Jack", 99))
    heap.print_heap()
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable
from random import choice


class IKey(ABC):

    @abstractmethod
    def key(self) -> int:
        ...


T = TypeVar("T", bound=IKey)


@dataclass
class Node(Generic[T]):
    data: T
    left: Optional['Node[T]'] = None
    right: Optional['Node[T]'] = None

    def key(self) -> int:
        return self.data.key()


class KeyNotFoundException(Exception):
    pass


class EmptyTreeException(Exception):
    pass


class IndexOutRangeException(Exception):
    pass


@dataclass
class Worker(IKey):
    name: str
    id: int

    def key(self) -> int:
        return self.id

    def __str__(self) -> str:
        return f"Worker({self.name},{self.id})"


class BinarySearchTree(Generic[T]):

    def __init__(self) -> None:
        self._length: int = 0
        self._root: Optional[Node[T]] = None

    def is_empty(self) -> bool:
        return self._length == 0

    def get_size(self) -> int:
        return self._length

    def size(self) -> int:
        return self._length

    def insert(self, value: T) -> None:
        new_node: Node[T] = Node(data=value)
        if self._root is None:
            self._root = new_node
            self._length += 1
        else:
            current_node = self._root
            while True:
                parent: Optional[Node[T]] = current_node
                if new_node.key() < current_node.key():
                    # двигаемся влево
                    current_node = current_node.left
                    if current_node is None:
                        parent.left = new_node
                        self._length += 1
                        return
                else:
                    # двигаемся вправо
                    current_node = current_node.right
                    if current_node is None:
                        parent.right = new_node
                        self._length += 1
                        return

    def remove(self, key: int) -> None:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")

        current_node = self._root
        parent_node = self._root
        is_left_node: bool = True
        while current_node.key() != key:
            parent_node = current_node
            if key < current_node.key():
                is_left_node = True
                current_node = current_node.left
            else:
                is_left_node = False
                current_node = current_node.right
            if current_node is None:
                raise KeyNotFoundException(f"KeyNotFoundException: {key}")

        # Если узел не имеет потомков, он просто удаляется
        if current_node.left is None and current_node.right is None:
            if current_node == self._root:
                self._root = None
            elif is_left_node:
                parent_node.left = None
            else:
                parent_node.right = None
        elif current_node.right is None:
            # Если нет правого потомка, узел заменяется левым поддеревом
            if current_node == self._root:
                self._root = current_node.left
            elif is_left_node:
                parent_node.left = current_node.left
            else:
                parent_node.right = current_node.left
        elif current_node.left is None:
            # Если нет левого потомка, узел заменяется правым поддеревом
            if current_node == self._root:
                self._root = current_node.right
            elif is_left_node:
                parent_node.left = current_node.right
            else:
                parent_node.right = current_node.right
        else:
            # Два потомка, узел заменяется преемником
            successor = self.__get_successor(current_node)

            # Родитель currentNode связывается с посредником
            if current_node == self._root:
                self._root = successor
            elif is_left_node:
                parent_node.left = successor
            else:
                parent_node.right = successor
            successor.left = current_node.left
        self._length -= 1

    def __get_successor(self, del_node: Node[T]) -> Node[T]:
        # Метод возвращает узел со следующим значением после удаляемого
        # сначала осуществляется переход к правому потомку, а затем
        # отслеживается цепочка левых потомков данного узла
        successor_parent = del_node
        successor = del_node
        current_node = del_node.right
        # Переход к правому потомку
        while current_node is not None:  # Пока остаются левые потомки
            successor_parent = successor
            successor = current_node
            current_node = current_node.left

        if successor != del_node.right:
            # Если преемник не является правым потомком создаются связи между узлами
            successor_parent.left = successor.right
            successor.right = del_node.right

        return successor

    def find(self, key: int) -> tuple[Optional[T], bool]:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")

        current_node = self._root
        while current_node.key() != key:
            if key < current_node.key():
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node is None:
                return None, False
        return current_node.data, True

    # ------------ симетричный обход дерева ------------
    def symmetric_traversal(self, func: Callable[[T], None]) -> None:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")
        self.__symmetric_traversal(self._root, func)

    def __symmetric_traversal(self, local_root: Optional[Node[T]],
                              func: Callable[[T], None]) -> None:
        if local_root is not None:
            self.__symmetric_traversal(local_root.left, func)
            func(local_root.data)
            self.__symmetric_traversal(local_root.right, func)

    # ------------ Неупорядоченный обход ------------
    def traversal_after_processing(self, func: Callable[[T], None]) -> None:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")
        self.__traversal_after_processing(self._root, func)

    def __traversal_after_processing(self, local_root: Optional[Node[T]],
                                     func: Callable[[T], None]) -> None:
        if local_root is not None:
            func(local_root.data)
            self.__symmetric_traversal(local_root.left, func)
            self.__symmetric_traversal(local_root.right, func)

    def traversal_before_processing(self, func: Callable[[T], None]) -> None:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")
        self.__traversal_before_processing(self._root, func)

    def __traversal_before_processing(self, local_root: Optional[Node[T]],
                                      func: Callable[[T], None]) -> None:
        if local_root is not None:
            self.__symmetric_traversal(local_root.left, func)
            self.__symmetric_traversal(local_root.right, func)
            func(local_root.data)

    # -------------------------------------------------

    def minimum(self) -> T:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")
        current_node = self._root
        last_node: Optional[Node[T]] = None
        while current_node is not None:
            last_node = current_node
            current_node = current_node.left
        return last_node.data

    def maximum(self) -> T:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")
        current_node = self._root
        last_node: Optional[Node[T]] = None
        while current_node is not None:
            last_node = current_node
            current_node = current_node.right
        return last_node.data

    def print_tree(self) -> None:
        result: list[str] = ["BinarySearchTree\n"]
        if not self.is_empty():
            self.__create_str_tree(result, "", self._root, True)
        print("".join(result))

    def __create_str_tree(self, result: list[str], prefix: str,
                          node: Optional[Node[T]], is_tail: bool ):
        if node.right is not None:
            new_prefix = prefix
            if is_tail:
                new_prefix += "│   "
            else:
                new_prefix += "    "
            self.__create_str_tree(result, new_prefix, node.right, False)

        result.append(prefix)
        if is_tail:
            result.append("└── ")
        else:
            result.append("┌── ")
        result.append(str(node.key())+"\n")

        if node.left is not None:
            new_prefix = prefix
            if is_tail:
                new_prefix += "    "
            else:
                new_prefix += "│   "
            self.__create_str_tree(result, new_prefix, node.left, True)


if __name__ == '__main__':
    workers: list[Worker] = [
        Worker("Max", 83), Worker("Alex", 58), Worker("Tom", 98), Worker("Tommy", 62), Worker("Max", 70),
        Worker("Alex", 34), Worker("Tom", 22), Worker("Max", 60), Worker("Alex", 99), Worker("Tom", 91),
        Worker("Tommy", 94), Worker("Tommy", 85),
    ]

    tree: BinarySearchTree[Worker] = BinarySearchTree[Worker]()
    for it in workers:
        tree.insert(it)
        print("----------------------------")
        print(f"Added: {it}")
        tree.print_tree()

    print("----- Find ------")
    value, ok = tree.find(62)
    print(f"Founded key value: {value}, ok == {ok}")

    print("----- Max key ------")
    value = tree.maximum()
    print(f"Max key value: {value}")

    print("----- Min key ------")
    value = tree.minimum()
    print(f"Min key value: {value}")

    print("----- Remove ------")
    removing_key = choice(workers)
    print(f"Remove node with key: {removing_key}")
    tree.remove(removing_key.key())
    tree.print_tree()

    # Варианты обхода дерева
    print("Symmetric traversal: [", end='')
    tree.symmetric_traversal(lambda worker: print(f"{worker.key()} ", end=''))
    print(f"]")

    print("Traversal after processing: [", end='')
    tree.traversal_after_processing(lambda worker: print(f"{worker.key()} ", end=''))
    print(f"]")

    print("Traversal before processing: [", end='')
    tree.traversal_before_processing(lambda worker: print(f"{worker.key()} ", end=''))
    print(f"]")

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
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
    height: int = 1

    def key(self) -> int:
        return self.data.key()


class KeyNotFoundException(Exception):
    pass


class EmptyTreeException(Exception):
    pass


@dataclass
class Worker(IKey):
    name: str
    id: int

    def key(self) -> int:
        return self.id

    def __str__(self) -> str:
        return f"Worker({self.name},{self.id})"


class AVLTree(Generic[T]):

    def __init__(self) -> None:
        self._length: int = 0
        self._root: Optional[Node[T]] = None

    def is_empty(self) -> bool:
        return self._length == 0

    def get_size(self) -> int:
        return self._length

    def __height(self, p: Optional[Node[T]]) -> int:
        if p is None:
            return 0
        return p.height

    def __bfactor(self, p: Optional[Node[T]]) -> int:
        return self.__height(p.right) - self.__height(p.left)

    def __update_height(self, p: Optional[Node[T]]) -> None:
        hl = self.__height(p.left)
        hr = self.__height(p.right)

        if hl > hr:
            p.height = hl + 1
        else:
            p.height = hr + 1

    def __rotate_right(self, p: Node[T]) -> Node[T]:
        q = p.left
        p.left = q.right
        q.right = p
        self.__update_height(p)
        self.__update_height(q)
        return q

    def __rotate_left(self, q: Node[T]) -> Node[T]:
        p = q.right
        q.right = p.left
        p.left = q
        self.__update_height(q)
        self.__update_height(p)
        return p

    def __balance(self, p: Node[T]) -> Node[T]:
        self.__update_height(p)
        if self.__bfactor(p) >= 2:
            if self.__bfactor(p.right) < 0:
                p.right = self.__rotate_right(p.right)
            return self.__rotate_left(p)
        if self.__bfactor(p) <= -2:
            if self.__bfactor(p.left) > 0:
                p.left = self.__rotate_left(p.left)
            return self.__rotate_right(p)
        return p

    def __insert(self, p: Optional[Node[T]], value: T) -> Node[T]:
        if p is None:
            return Node[T](data=value)
        if value.key() < p.key():
            p.left = self.__insert(p.left, value)
        else:
            p.right = self.__insert(p.right, value)
        return self.__balance(p)

    def insert(self, value: T) -> None:
        self._root = self.__insert(self._root, value)
        self._length += 1

    def __find_Minimum_root_Node(self, node: Optional[Node[T]]) -> Node[T]:
        current_node = node.left
        if current_node is None:
            return node
        while current_node.left is not None:
            current_node = current_node.left

        return current_node

    def __remove_node_with_min_key(self, node: Optional[Node[T]]) -> Node[T]:
        if node.left is None:
            return node.right
        node.left = self.__remove_node_with_min_key(node.left)
        return self.__balance(node)

    def __remove(self, node: Optional[Node[T]], key: int) ->  Optional[Node[T]]:
        if node is None:
            return None

        if key < node.key():
            node.left = self.__remove(node.left, key)
        elif key > node.key():
            node.right = self.__remove(node.right, key)
        else:  # найден узел с необходимым значением ключа
            q = node.left
            r = node.right
            node = None
            if r is None:
                return q

            min_node = self.__find_Minimum_root_Node(r)
            min_node.right = self.__remove_node_with_min_key(r)
            min_node.left = q
            return self.__balance(min_node)
        return self.__balance(node)

    def remove(self, key: int) -> None:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")

        _, ok = self.find(key)
        if not ok:
            raise KeyNotFoundException("KeyNotFoundException")
        self._root = self.__remove(self._root, key)
        self._length -= 1

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
        result: list[str] = ["AVLTree\n"]
        if not self.is_empty():
            self.__create_str_tree(result, "", self._root, True)
        print("".join(result))

    def __create_str_tree(self, result: list[str], prefix: str,
                          node: Optional[Node[T]], is_tail: bool):
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
        result.append(str(node.key()) + "\n")

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

    tree: AVLTree[Worker] = AVLTree[Worker]()
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


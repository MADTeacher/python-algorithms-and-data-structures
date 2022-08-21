from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable


T = TypeVar("T")


class EmptyKeyException(Exception):
    pass

class EmptyPrefixException(Exception):
    pass


@dataclass
class Node(Generic[T]):
    label: str
    value: Optional[T] = None
    key: str = ""
    left: Optional['Node[T]'] = None
    right: Optional['Node[T]'] = None
    middle: Optional['Node[T]'] = None
    is_end: bool = False


@dataclass
class Worker:
    name: str
    id: int

    def __str__(self) -> str:
        return f"Worker({self.name},{self.id})"


class Trie(Generic[T]):

    def __init__(self) -> None:
        self._length: int = 0
        self._root: Optional[Node[T]] = None

    def is_empty(self) -> bool:
        return self._length == 0

    def get_size(self) -> int:
        return self._length

    def __find_node(self, node:  Optional[Node[T]],
                    key: str, index: int) -> Optional[Node[T]]:
        if node is Node or len(key) == 0:
            return None

        c = key[index]
        if c < node.label:
            return self.__find_node(node.left, key, index)
        elif c > node.label:
            return self.__find_node(node.right, key, index)
        elif index < len(key) - 1:
            return self.__find_node(node.middle, key, index + 1)
        else:
            return node

    def get(self, key: str) -> tuple[Optional[T], bool]:
        if len(key) == 0:
            return None, False
        x = self.__find_node(self._root, key, 0)
        if x is None or not x.is_end:
            return None, False
        return x.value, True

    def contains(self, key: str) -> bool:
        if len(key) == 0:
            return False
        _, ok = self.get(key)
        return ok

    def put(self, key: str, value: T):
        if len(key) == 0:
            raise EmptyKeyException("EmptyKeyException")
        self._root = self.__put(self._root, key, value, 0, True)
        self._length += 1

    def __put(self, node:  Optional[Node[T]], key: str,
              value: T, index: int, is_end: bool) -> Node[T]:
        label = key[index]
        if node is None:
            node = Node[T](label=label)

        if label < node.label:
            node.left = self.__put(node.left, key, value, index, is_end)
        elif label > node.label:
            node.right = self.__put(node.right, key, value, index, is_end)
        elif index < len(key) - 1:
            node.middle = self.__put(node.middle, key, value, index + 1, is_end)
        else:
            node.value = value
            node.is_end = is_end
            node.key = key
        return node

    def remove(self, key: str):
        if len(key) == 0 or not self.contains(key):
            return
        self._root = self.__put(self._root, key, None, 0, False)
        self._length -= 1

    def longest_prefix(self, query: str) -> str:
        if len(query) == 0:
            return ""

        length: int = 0
        current_node = self._root
        i: int = 0
        while current_node is not None and i < len(query):
            label = query[i]
            if label < current_node.label:
                current_node = current_node.left
            elif label > current_node.label:
                current_node = current_node.right
            else:
                i += 1
                if current_node.is_end:
                    length = i
                current_node = current_node.middle
        return query[:length]

    def __assemble(self,  node:  Optional[Node[T]], prefix: str, queue: list[str]) -> list[str]:
        if node is None:
            return queue

        queue = self.__assemble(node.left, prefix, queue)
        if node.is_end:
            queue.append(prefix + node.label)
        queue = self.__assemble(node.middle, prefix + node.label, queue)
        return self.__assemble(node.right, prefix, queue)

    def all_keys(self) -> list[str]:
        keys: list[str] = []
        return self.__assemble(self._root, "", keys)

    def all_keys_with_prefix(self, prefix: str) -> list[str]:
        if len(prefix) == 0:
            raise EmptyPrefixException("EmptyPrefixException")

        x = self.__find_node(self._root, prefix, 0)
        if x is None:
            return list[str]()
        keys: list[str] = []
        if x.is_end:
            keys.append(prefix)
        return self.__assemble(x.middle, prefix, keys)

    def for_each(self, func: Callable[[str, T], None]):
        if self.is_empty():
            return
        self.__for_each(self._root, func)

    def __for_each(self, local_root:  Optional[Node[T]],
                   func: Callable[[str, T], None]):
        if local_root is not None:
            if local_root.is_end:
                func(local_root.key, local_root.value)
            self.__for_each(local_root.left, func)
            self.__for_each(local_root.middle, func)
            self.__for_each(local_root.right, func)


if __name__ == '__main__':
    def print_trie(key: str, value: T) -> None:
        print(f"Key: {key}; Value: {value}")

    data: dict[str, list[Worker]] = {
        "manager": [Worker("Julie", 1), Worker("Alex", 2), Worker("Tom", 4)],
        "policeman": [Worker("George", 3), Worker("Max", 60)],
        "postman": [Worker("Tommy", 94), Worker("William", 12)],
        "mathematician": [Worker("Sophia", 14), Worker("Oliver", 13)],
        "postwoman": [Worker("Sandra", 91), Worker("Ann", 6)],
        "policewoman": [Worker("Elizabeth", 9), Worker("Kate", 20)],
    }

    trie: Trie[list[Worker]] = Trie[list[Worker]]()
    for key, value in data.items():
        trie.put(key, value)

    trie.for_each(print_trie)
    print()
    print(f"'man' is Contains? {trie.contains('man')}")
    print(f"'manager' is Contains? {trie.contains('manager')}")
    print(f"Keys with prefix 'po': {trie.all_keys_with_prefix('po')}")
    print(f"Keys with prefix 'police': {trie.all_keys_with_prefix('police')}")
    print(f"Keys with prefix 'm': {trie.all_keys_with_prefix('m')}")
    print(f"All keys: {trie.all_keys()}")
    print()
    print("----- Remove key 'manager'------")
    trie.remove("manager")

    trie.for_each(print_trie)

from dataclasses import dataclass
from typing import Optional
from heap import Heap, IKey


def _calc_frequency(text: str) -> dict[str, int]:
    frequency_array: dict[str, int] = {}
    for it in text:
        if it in frequency_array:
            frequency_array[it] += 1
        else:
            frequency_array[it] = 1

    return frequency_array


@dataclass
class Index:
    _index: int

    def increment(self) -> None:
        self._index += 1

    def value(self) -> int:
        return self._index


@dataclass
class HuffmanNode(IKey):
    frequency: int
    symbol: str = ""
    right_child: Optional['HuffmanNode'] = None
    left_child: Optional['HuffmanNode'] = None
    leaf: bool = False

    def is_leaf(self) -> bool:
        return self.leaf

    def get_symbol(self) -> str:
        return self.symbol

    def key(self) -> int:
        return self.frequency

    @staticmethod
    def new_node(left: 'HuffmanNode', right: 'HuffmanNode')-> 'HuffmanNode':
        return HuffmanNode(
            frequency=left.frequency + right.frequency,
            left_child=left,
            right_child=right
        )

    @staticmethod
    def new_leaf(frequency: int, symbol: str) -> 'HuffmanNode':
        return HuffmanNode(
            frequency=frequency,
            symbol=symbol,
            leaf=True
        )


class HuffmanTree:
    def __init__(self, root: HuffmanNode) -> None:
        self.frequency: int = root.frequency
        self.root: Optional[HuffmanNode] = root
        self.huffman_code: dict[str, str] = {}
        self.encodedString: str = ""

    def get_root(self) -> HuffmanNode:
        return self.root

    def print_huffman_code(self) -> None:
        print("------HuffmanCode------")
        for k, v in self.huffman_code.items():
            print(f"{k}: {v}")

    def __encode(self, root: Optional[HuffmanNode], symbol: str) -> None:
        if root is None:
            return
        if root.is_leaf():
            if symbol == "":
                self.huffman_code[root.symbol] = "1"
            else:
                self.huffman_code[root.symbol] = symbol
        self.__encode(root.left_child, symbol + "0")
        self.__encode(root.right_child, symbol + "1")

    def get_encoded_text(self) -> str:
        return self.encodedString

    def __decode(self, root: Optional[HuffmanNode], index: Index,
                 coded_data: str,  text: list[str]) -> None:
        if root is None:
            return

        if root.is_leaf():
            text.append(root.symbol)
            return

        index.increment()

        if coded_data[index.value()] == "0":
            self.__decode(root.left_child, index, coded_data, text)
        else:
            self.__decode(root.right_child, index, coded_data, text)

    def get_decoded_string(self, data: str) -> str:
        text: list[str] = []
        index: Index = Index(-1)

        if self.root.is_leaf():
            # для случаев входного текста типа: ААА, аа и т.д.
            while self.root.frequency > 0:
                text.append(self.root.symbol)
                self.frequency -= 1
        else:
            while index.value() < len(data) - 1:
                self.__decode(self.root, index, data, text)

        return "".join(text)

    @staticmethod
    def create_huffman_tree(text: str) -> 'HuffmanTree':
        data = _calc_frequency(text)
        heap = Heap[HuffmanNode](len(data))
        for symbol, frequency in data.items():
            heap.insert(HuffmanNode.new_leaf(frequency, symbol))

        while heap.get_size() > 1:
            first_node = heap.remove()
            second_node = heap.remove()
            heap.insert(HuffmanNode.new_node(first_node, second_node))

        root: HuffmanNode = heap.remove()
        tree = HuffmanTree(root)
        tree.__encode(tree.root, "")
        for it in text:
            tree.encodedString += tree.huffman_code[it]

        return tree

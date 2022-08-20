from dataclasses import dataclass
from typing import Generic, Optional

from my_collections import Heap, IKey, MySet
from graph import Graph, T, AdjacentEdge, Edge


@dataclass
class _PrimNode(Generic[T], IKey):
    start: T
    finish: T
    weight: int

    def key(self) -> int:
        return self.weight

    def name(self) -> str:
        return f"{self.start}"


def prim(graph: Graph[T], start: T) -> Graph[T]:
    my_set: MySet[T] = MySet[T]()
    mst = Graph[T]()

    my_set.add(start)
    while my_set.size() != graph.amount_vertexes():
        heap = Heap[_PrimNode[T]](graph.amount_edges())

        def foreach(vertex: T) -> None:
            def edges_foreach(edge: AdjacentEdge[T]) -> None:
                if my_set.contains(edge.finish_edge):
                    return
                heap.insert(_PrimNode(vertex, edge.finish_edge, edge.weight))
            graph.for_each_adjacent_edge(vertex, edges_foreach)
        my_set.for_each(foreach)

        while not heap.is_empty():
            edge: _PrimNode[T] = heap.remove()
            mst.add_edge(edge.start, edge.finish, edge.weight)
            my_set.add(edge.finish)
            break

    return mst


if __name__ == '__main__':
    vertexes: list[Edge[str]] = [
        Edge("A", "B", 13),
        Edge("A", "C", 6),
        Edge("A", "F", 4),
        Edge("B", "C", 7),
        Edge("B", "F", 7),
        Edge("B", "E", 5),
        Edge("C", "E", 1),
        Edge("C", "F", 8),
        Edge("E", "F", 9),
    ]

    graph: Graph[str] = Graph[str]()

    for it in vertexes:
        graph.add_edge(it.start_edge, it.finish_edge, it.weight)

    mst = prim(graph, "C")
    print(mst.amount_vertexes() == graph.amount_vertexes())
    print("---------Vertexes-----------")
    mst.print_all_vertexes()
    print("---------Edges-----------")
    mst.print_all_edges()
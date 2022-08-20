from typing import Callable

from my_collections import MySet, Queue
from graph import Graph, T, AdjacentEdge, Edge


def bsf(graph: Graph[T], start: T, walkfunc: Callable[[T], bool]) -> None:
    queue = Queue[T]()
    visited = MySet[T]()
    queue.enqueue(start)

    def __foreach(edge: AdjacentEdge[T]) -> None:
        if not visited.contains(edge.finish_edge):
            queue.enqueue(edge.finish_edge)

    while not queue.is_empty():
        vertex = queue.dequeue()

        if walkfunc(vertex):
            return

        visited.add(vertex)

        graph.for_each_adjacent_edge(vertex, __foreach)


if __name__ == '__main__':
    vertexes: list[Edge[str]] = [
        Edge("A", "B"),
        Edge("A", "C"),
        Edge("C", "F"),
        Edge("C", "G"),
        Edge("G", "M"),
        Edge("G", "N"),
        Edge("B", "D"),
        Edge("B", "E"),
        Edge("D", "H"),
        Edge("D", "I"),
        Edge("D", "J"),
        Edge("E", "K"),
        Edge("E", "L"),
    ]

    graph: Graph[str] = Graph[str]()

    for it in vertexes:
        graph.add_edge_without_weight(it.start_edge, it.finish_edge)

    def bsf_walk(vertex: str) -> bool:
        print(vertex + " ", end='')
        return vertex == "K"

    bsf(graph, "A", bsf_walk)
    print()
    # ----------------Path---------------------
    path: list[str] = []

    def bsf_walk_with_path(vertex: str) -> bool:
        path.append(vertex)
        return vertex == "K"

    bsf(graph, "A", bsf_walk_with_path)
    print()

    path.reverse()
    min_path: list[str] = ["K"]
    find: str = "K"
    for vertex in path:
        if graph.vertexes[vertex].contains(AdjacentEdge[str](find)):
            min_path.append(vertex)
            find = vertex

    min_path.reverse()
    print(min_path)

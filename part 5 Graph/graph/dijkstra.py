import math
from dataclasses import dataclass
from typing import Generic, Optional

from my_collections import Heap, IKey
from graph import Graph, T, AdjacentEdge, Edge


@dataclass
class _DijkstraNode(Generic[T], IKey):
    vertex: T
    distance: int
    predecessor: Optional['_DijkstraNode[T]'] = None

    def key(self) -> int:
        return self.distance

    def name(self) -> str:
        return f"{self.vertex}"


def dijkstra(graph: Graph[T], start: T, end: T) -> tuple[list[T], int]:
    heap = Heap[_DijkstraNode[T]](graph.amount_vertexes(), True)
    nodes: dict[T, _DijkstraNode[T]] = {}

    def foreach_init(vertex: T):
        node = _DijkstraNode[T](vertex, math.inf)
        heap.insert(node)
        nodes[vertex] = node

    graph.for_each_vertex(foreach_init)

    # устанавливаем значение пути начальной вершины в 0
    nodes[start].distance = 0
    heap.change(nodes[start])

    # реализуем обход и расчет пути для каждой из вершины, начиная с
    # вершины start до тех пор, пока не дойдем
    # до вершины end
    while not heap.is_empty():
        v: _DijkstraNode[T] = heap.remove()

        def calc(edge: AdjacentEdge[T]):
            node = nodes[edge.finish_edge]

            if node is None:
                return

            if v.distance + edge.weight < node.distance:
                node.distance = v.distance + edge.weight
                node.predecessor = v
                heap.change(node)
        graph.for_each_adjacent_edge(v.vertex, calc)

        if v.vertex == end:
            path: list[T] = []
            cost = v.distance
            it = v
            while it is not None:
                path.append(it.vertex)
                it = it.predecessor
            return path, cost
    return [], 0


if __name__ == '__main__':
    vertexes: list[Edge[str]] = [
        Edge("A", "B", 8),
        Edge("A", "C", 5),
        Edge("B", "D", 1),
        Edge("B", "E", 13),
        Edge("C", "F", 14),
        Edge("C", "D", 10),
        Edge("F", "D", 9),
        Edge("F", "E", 6),
        Edge("D", "E", 8),
    ]

    graph: Graph[str] = Graph[str]()

    for it in vertexes:
        graph.add_edge(it.start_edge, it.finish_edge, it.weight)

    path, cost = dijkstra(graph, "E", "A")
    print(f"Path: {path} with cost: {cost}")

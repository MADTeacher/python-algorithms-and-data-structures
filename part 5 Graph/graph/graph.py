from dataclasses import dataclass
from typing import TypeVar, Generic, Callable

from my_collections import MySet

T = TypeVar("T")


@dataclass
class Edge(Generic[T]):
    start_edge: T
    finish_edge: T
    weight: int = 0


@dataclass
class AdjacentEdge(Generic[T]):
    finish_edge: T
    weight: int = 0

    def __hash__(self) -> int:
        return hash((self.finish_edge, self.weight))


class Graph(Generic[T]):
    def __init__(self, is_directed: bool = False) -> None:
        self.vertexes: dict[T, MySet[AdjacentEdge[T]]] = {}
        self.is_not_directed: bool = not is_directed

    def add_vertex(self, vertex: T) -> None:
        if vertex not in self.vertexes:
            self.vertexes[vertex] = MySet[AdjacentEdge[T]]()

    def add_edge(self, vertex1: T, vertex2: T, weight: int) -> None:
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.vertexes[vertex1].add(AdjacentEdge[T](vertex2, weight))
        if self.is_not_directed:
            self.vertexes[vertex2].add(AdjacentEdge[T](vertex1, weight))

    def add_edge_without_weight(self, vertex1: T, vertex2: T) -> None:
        self.add_edge(vertex1, vertex2, 0)

    def for_each_vertex(self, func: Callable[[T], None]) -> None:
        for v, _ in self.vertexes.items():
            func(v)

    def for_each_edge(self, func: Callable[[Edge[T]], None]) -> None:
        for vertex1, edges in self.vertexes.items():
            def edge_creator(value: AdjacentEdge[T]) -> None:
                func(Edge[T](vertex1, value.finish_edge, value.weight))

            edges.for_each(edge_creator)

    def for_each_adjacent_edge(self, vertex: T, func: Callable[[AdjacentEdge[T]], None]):
        if vertex in self.vertexes:
            edges = self.vertexes[vertex]
            edges.for_each(lambda x: func(x))

    def amount_edges(self) -> int:
        count: int = 0
        for _, edges in self.vertexes.items():
            count += edges.size()

        if self.is_not_directed:
            count //= 2

        return count

    def amount_vertexes(self) -> int:
        return len(self.vertexes)

    def print_all_edges(self) -> None:
        def print_edge(edge: Edge[T]) -> None:
            print(f"Edge(V1: {edge.start_edge}, V2: {edge.finish_edge}, Weight: {edge.weight})")
        self.for_each_edge(print_edge)

    def print_all_vertexes(self) -> None:
        def print_vertex(vertex: T) -> None:
            print(f"Vertex: {vertex}")
        self.for_each_vertex(print_vertex)


if __name__ == '__main__':

    @dataclass
    class City:
        name: str
        id: int

        def __str__(self) -> str:
            return f"City({self.name},{self.id})"

        def __hash__(self) -> int:
            return hash((self.name, self.id))

    city_list: list[City] = [City("Saint Petersburg", 2), City("Moscow", 1),
                             City("Pskov", 3),City("Rostov-on-Don", 4),
                             City("Stavropol", 5), City("Grozny", 7),
                             City("Gukovo", 6), City("Kalach-na-Donu", 14),
                             City("Kansk", 13), City("Mamonovo", 91),
                             City("Nizhnekamsk", 8), City("Omsk", 9),
                             City("Oryol", 20)]

    graph = Graph[City]()

    for it in city_list:
        graph.add_vertex(it)

    graph.add_edge(city_list[0], city_list[3], 1960)
    graph.add_edge(city_list[0], city_list[1], 1500)
    graph.add_edge(city_list[1], city_list[3], 460)
    graph.add_edge(city_list[3], city_list[6], 100)

    print(len(city_list) == graph.amount_vertexes())
    print("---------Vertexes-----------")
    graph.print_all_vertexes()
    print("---------Edges-----------")
    graph.print_all_edges()

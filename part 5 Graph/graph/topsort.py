from graph import Graph, T, AdjacentEdge, Edge


def topological_sort(graph: Graph[T]) -> tuple[list[T], dict[T, int], bool]:
    in_degree: dict[T, int] = {}

    def dec_degree(edge: AdjacentEdge[T]) -> None:
        in_degree[edge.finish_edge] -= 1

    def foreach_edge(edge: Edge[T]):
        if edge.start_edge not in in_degree:
            in_degree[edge.start_edge] = 0

        if edge.finish_edge in in_degree:
            in_degree[edge.finish_edge] += 1
        else:
            in_degree[edge.finish_edge] = 1
    graph.for_each_edge(foreach_edge)

    result_list: list[T] = []
    result_dict: dict[T, int] = {}
    count_level: int = 0
    while len(in_degree) > 0:
        temp_list: list[T] = []
        for vertex, degree in in_degree.items():
            if degree == 0:
                temp_list.append(vertex)
                result_dict[vertex] = count_level

        if len(temp_list) == 0:
            return [], {}, False

        for vertex in temp_list:
            graph.for_each_adjacent_edge(vertex, dec_degree)
            del in_degree[vertex]
            result_list.append(vertex)

        count_level += 1

    return result_list, result_dict, True


if __name__ == '__main__':
    graph = Graph[str](is_directed=True)

    graph.add_edge_without_weight("A", "B")
    graph.add_edge_without_weight("A", "D")
    graph.add_edge_without_weight("B", "C")
    graph.add_edge_without_weight("B", "D")
    graph.add_edge_without_weight("C", "E")
    graph.add_edge_without_weight("D", "E")
    graph.add_edge_without_weight("D", "F")
    graph.add_edge_without_weight("E", "F")

    top_list, top_dict, ok = topological_sort(graph)
    print(top_list)
    print(top_dict)

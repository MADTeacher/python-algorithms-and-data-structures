import sys


def find_min_route(tsp: list[list[int]], start_city: int) -> tuple[int, list[int]]:
    result_sum: int = 0
    counter: int = 0
    min_value: int = sys.maxsize

    visited_city: dict[int, None] = {start_city: None}
    route: list[int] = [0 for _ in range(0, len(tsp))]

    i: int = 0
    j: int = start_city

    while i < len(tsp) and j < len(tsp[i]):
        if counter >= len(tsp[i]) - 1:
            break

        if j != i and j not in visited_city:
            if tsp[i][j] < min_value:
                min_value = tsp[i][j]
                route[counter] = j + 1

        j += 1

        if j == len(tsp[i]):
            result_sum += min_value
            min_value = sys.maxsize
            visited_city[route[counter]-1] = None
            j = 0
            i = route[counter] - 1
            counter += 1

    i = route[counter - 1] - 1
    result_sum += tsp[i][start_city]
    route[counter] = start_city + 1
    route.insert(0, start_city+1)
    return result_sum, route


if __name__ == '__main__':
    tsp: list[list[int]] = [
        [-1, 10, 15, 20],
        [10, -1, 35, 25],
        [15, 35, -1, 30],
        [20, 25, 30, -1],
    ]
    profit, route = find_min_route(tsp, 1)
    print(f"Profit: {profit}, route: {route}")

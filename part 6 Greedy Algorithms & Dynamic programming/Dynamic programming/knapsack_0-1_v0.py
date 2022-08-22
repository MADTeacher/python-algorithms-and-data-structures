from dataclasses import dataclass


@dataclass
class Item:
    cost: int
    weight: int
    item_id: int


def knapsack(knapsack_capacity: int, n: int,
             items: list[Item]) -> int:
    if n == 0 or knapsack_capacity == 0:
        return 0

    if items[n - 1].weight > knapsack_capacity:
        return knapsack(knapsack_capacity, n - 1, items)
    else:
        return max(
            items[n - 1].cost + knapsack(knapsack_capacity - items[n - 1].weight, n - 1, items),
            knapsack(knapsack_capacity, n - 1, items)
        )


if __name__ == "__main__":
    knapsack_capacity = 50

    items: list[Item] = [
        Item(60, 10, 1),
        Item(100, 20, 10),
        Item(120, 30, 5),
        Item(100, 25, 6),
        Item(90, 19, 7),
    ]

    result = knapsack(knapsack_capacity, len(items), items)
    print(f"Max cost: {result}")

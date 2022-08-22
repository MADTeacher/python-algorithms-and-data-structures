from dataclasses import dataclass


@dataclass
class Item:
    cost: int
    weight: int
    item_id: int


def knapsack(knapsack_capacity: int, n: int,
             items: list[Item]) -> int:
    dp: list[int] = [0 for _ in range(0, knapsack_capacity + 1)]
    i = 1
    while i < len(items) + 1:
        w = knapsack_capacity
        while w >= 0:
            if items[i - 1].weight <= w:
                item = items[i - 1]
                dp[w] = max(dp[w], dp[w - item.weight] + item.cost)
            w -= 1
        i += 1
    return dp[knapsack_capacity]


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

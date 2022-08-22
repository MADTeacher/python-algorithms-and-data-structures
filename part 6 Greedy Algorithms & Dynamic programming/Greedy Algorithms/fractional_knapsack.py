from dataclasses import dataclass


@dataclass
class Item:
    cost: int
    weight: int
    item_id: int

    def __lt__(self, other: 'Item') -> bool:
        a = self.cost / self.weight
        b = other.cost / other.weight
        return a > b


def fractional_knapsack(knapsack_capacity: int,
                        items: list[Item]) -> tuple[float, list[Item]]:
    final_cost: float = 0
    knapsack: list[Item] = []
    items.sort()
    for it in items:
        if it.weight <= knapsack_capacity:
            knapsack_capacity -= it.weight
            final_cost += it.cost
            knapsack.append(it)
        else:
            weight = knapsack_capacity / it.weight
            last_cost = it.cost * weight
            final_cost += last_cost
            knapsack.append(Item(int(last_cost), int(weight), it.item_id))
            break
    return final_cost, knapsack


if __name__ == '__main__':
    knapsack_capacity = 50
    items: list[Item] = [
        Item(60, 15, 1),
        Item(100, 10, 10),
        Item(300, 50, 5)
    ]
    max_cost, knapsack = fractional_knapsack(knapsack_capacity, items)
    print(max_cost, knapsack)

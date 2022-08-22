from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    task_id: int
    deadline: int
    profit: int
    description: str

    def __lt__(self, other: 'Task') -> bool:
        return self.profit > other.profit


def schedule_tasks(tasks: list[Task], max_day: int) -> tuple[int, list[Task]]:
    profit: int = 0
    slot: list[Optional[Task]] = [None for _ in range(0, max_day)]

    tasks.sort()

    for idx, task in enumerate(tasks):
        j = task.deadline - 1
        while j >= 0:
            if j < max_day and slot[j] is None:
                slot[j] = tasks[idx]
                profit += task.profit
                break
            j -= 1

    result_tasks: list[Task] = []
    for it in slot:
        if it is not None:
            result_tasks.append(it)

    return profit, result_tasks


if __name__ == '__main__':
    tasks: list[Task] = [
        Task(1, 9, 15, "Уборка"),
        Task(2, 2, 2, "Запилить баг"),
        Task(3, 5, 18, "Пофиксить баг"),
        Task(4, 7, 1, "Сварить кофе"),
        Task(5, 4, 25, "Участие в совещании"),
        Task(6, 2, 20, "One-to-one"),
        Task(7, 5, 8, "Ревью кода"),
        Task(8, 7, 10, "Погладить одежду"),
        Task(9, 4, 12, "Разработать фичу"),
        Task(10, 3, 5, "Кричать: 'За что???'"),
    ]

    profit, optimal_tasks = schedule_tasks(tasks, 15)
    print(f"Profit: {profit}")
    print("Optimal tasks:")
    for it in optimal_tasks:
        print(it)

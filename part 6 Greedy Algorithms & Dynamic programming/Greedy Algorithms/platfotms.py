from dataclasses import dataclass


@dataclass
class Train:
    arrival: float
    departure: float
    train_id: int


def find_min_platforms(trains: list[Train]) -> int:
    platforms: int = 0
    count: int = 0
    arrivals = trains
    departure = arrivals.copy()

    arrivals.sort(key=lambda it: it.arrival)
    departure.sort(key=lambda it: it.departure)

    i = j = 0
    while i < len(trains):
        if arrivals[i].arrival < departure[j].departure:
            count += 1
            platforms = max(count, platforms)
            i += 1
            # переходим к рассмотрению времени следующего пребывающего поезда
        else:
            count -= 1
            j += 1
            # переходим к рассмотрению времени отправления следующего поезда
    return platforms


if __name__ == '__main__':
    trains: list[Train] = [
        Train(2.00, 2.30, 1),
        Train(2.10, 3.40, 10),
        Train(3.00, 3.20, 5),
        Train(3.20, 4.30, 6),
        Train(3.15, 4.00, 7),
        Train(4.50, 5.10, 2),
    ]
    platforms = find_min_platforms(trains)
    print(f"Platforms: {platforms}")

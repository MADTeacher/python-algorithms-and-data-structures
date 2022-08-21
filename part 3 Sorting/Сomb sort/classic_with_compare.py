from collections.abc import Callable


def comb_sort(arr: list[int], comp: Callable[[int, int], bool]) -> None:
    if len(arr) == 0:
        raise ValueError("array is empty")

    def swap(i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    factor = 1.247
    step = len(arr) - 1
    while step >= 1:
        i = 0
        while i + step < len(arr):
            if comp(arr[i], arr[i + int(step)]):
                swap(i, i + int(step))
            i += 1
        step /= factor
    return arr


if __name__ == '__main__':
    arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
    arr_clone = arr.copy()
    print(f"Array before sort: {arr}")
    comb_sort(arr, lambda i, j: i > j)
    print(f"Array after ascending sorting: {arr}")
    comb_sort(arr_clone, lambda i, j: i < j)
    print(f"Array after descending sorting: {arr_clone}")
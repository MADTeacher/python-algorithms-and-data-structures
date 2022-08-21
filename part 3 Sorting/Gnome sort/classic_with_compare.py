from collections.abc import Callable


def gnome_sort(arr: list[int], comp: Callable[[int, int], bool]) -> None:
    if len(arr) == 0:
        raise ValueError("array is empty")

    def swap(i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    i = 1
    while i < len(arr):
        if comp(arr[i], arr[i - 1]):
            i += 1
        else:
            swap(i, i - 1)
            if i > 1:
                i -= 1


if __name__ == '__main__':
    arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
    arr_clone = arr.copy()
    print(f"Array before sort: {arr}")
    gnome_sort(arr, lambda i, j: i > j)
    print(f"Array after ascending sorting: {arr}")
    gnome_sort(arr_clone, lambda i, j: i < j)
    print(f"Array after descending sorting: {arr_clone}")

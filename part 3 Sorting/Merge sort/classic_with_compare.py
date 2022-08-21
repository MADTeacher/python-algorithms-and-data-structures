from collections.abc import Callable

def merge_sort_impl(arr: list[int], buffer: list[int],
                    l: int, r: int, comp: Callable[[int, int], bool]) -> None:
    if l < r:
        m = (l + r) // 2
        merge_sort_impl(arr, buffer, l, m, comp)
        merge_sort_impl(arr, buffer, m + 1, r, comp)

        k, j = l, m + 1
        i = l
        while i <= m or j <= r:
            if j > r or (i <= m and comp(arr[i], arr[j])):
                buffer[k] = arr[i]
                i += 1
            else:
                buffer[k] = arr[j]
                j += 1
            k += 1

        for i in range(l, r + 1):
            arr[i] = buffer[i]


def merge_sort(arr: list[int], comp: Callable[[int, int], bool]) -> list[int]:
    if len(arr) == 0:
        raise ValueError("array is empty")

    buffer = [0 for _ in range(len(arr))]
    merge_sort_impl(arr, buffer, 0, len(arr) - 1, comp)


if __name__ == '__main__':
    arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
    arr_copy = arr.copy()
    print(f"Array before sort: {arr}")
    merge_sort(arr, lambda i, j: i < j)
    print(f"Array after ascending sorting: {arr}")
    merge_sort(arr_copy, lambda i, j: i > j)
    print(f"Array after descending sorting: {arr_copy}")

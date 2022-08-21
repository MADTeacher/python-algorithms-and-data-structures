from collections.abc import Callable


def cocktail_sort(arr: list[int], comp: Callable[[int, int], bool]) -> None:
    if len(arr) == 0:
        raise ValueError("array is empty")

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    left = 0
    right = len(arr) - 1

    while left <= right:
        for i in range(right, left, -1):
            if comp(arr[i - 1], arr[i]):
                swap(i - 1, i)
        left += 1
        for i in range(left, right):
            if comp(arr[i], arr[i + 1]):
                swap(i, i + 1)
        right -= 1

if __name__ == '__main__':
    arr = [1, 2, 6, 0, -2, -4, 22, 54, 109, 5, 3]
    arr_copy = arr.copy()
    print(f"Array before sort: {arr}")
    cocktail_sort(arr, lambda i, j: i > j)
    print(f"Array after ascending sorting: {arr}")
    cocktail_sort(arr_copy, lambda i, j: i < j)
    print(f"Array after descending sorting: {arr_copy}")

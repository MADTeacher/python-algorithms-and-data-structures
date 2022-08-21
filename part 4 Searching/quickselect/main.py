import random


def quick_select(arr: list[int], k: int) -> int:
    if len(arr) == 1:
        return arr[0]

    pivot = arr[random.randint(0, len(arr) - 1)]
    L: list[int] = []
    M: list[int] = []
    R: list[int] = []
    for val in arr:
        if pivot > val:
            L.append(val)

        if pivot == val:
            M.append(val)

        if pivot < val:
            R.append(val)

    if k <= len(L):
        return quick_select(L, k)
    elif k <= (len(L) + len(M)):
        return pivot
    else:
        return quick_select(R, k - (len(L) + len(M)))


if __name__ == '__main__':
    arr = [3, -2, 0, 4, 22, -1, 34, 10, 5, 7, 9]

    print(f"Array: {arr}")
    k = 3
    kMin = quick_select(arr, k)
    print(f"{k}-th min element is: {kMin}")  # 3-th min element is: 0
    k = 2
    kMin = quick_select(arr, k)
    print(f"{k}-th min element is: {kMin}")  # 2-th min element is: -1
    k = 5
    kMin = quick_select(arr, k)
    print(f"{k}-th min element is: {kMin}")  # 5-th min element is: 4

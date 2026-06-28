from typing import List


def maximum_element_after_decrementing_and_rearranging(arr: List[int]) -> int:
    arr.sort()
    n = len(arr)

    arr[0] = 1
    for i in range(1, n):
        arr[i] = min(arr[i], arr[i - 1] + 1)

    return arr[-1]


print(maximum_element_after_decrementing_and_rearranging([2, 2, 1, 2, 1]))
print(maximum_element_after_decrementing_and_rearranging([100, 1, 1000]))
print(maximum_element_after_decrementing_and_rearranging([1, 2, 3, 4, 5]))

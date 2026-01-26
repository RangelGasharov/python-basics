def minimum_abs_difference(arr: list[int]) -> list[list[int]]:
    arr.sort()
    result = []
    min_difference = float("inf")
    n = len(arr)
    for i in range(n - 1):
        current = arr[i + 1] - arr[i]
        if min_difference > current:
            min_difference = current
            result = []
        if current == min_difference:
            result.append([arr[i], arr[i + 1]])
    return result

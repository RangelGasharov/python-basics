def maxPower(stations: list[int], r: int, k: int) -> int:
    n = len(stations)
    count = [0] * (n + 1)

    for i in range(n):
        left = max(0, i - r)
        right = min(n, i + r + 1)
        count[left] += stations[i]
        count[right] -= stations[i]

    def check(val: int) -> bool:
        diff = count.copy()
        total = 0
        remaining = k

        for j in range(n):
            total += diff[j]
            if total < val:
                add = val - total
                if remaining < add:
                    return False
                remaining -= add
                end = min(n, j + 2 * r + 1)
                diff[end] -= add
                total += add
        return True

    low, high = min(stations), sum(stations) + k
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result


print(maxPower([1, 2, 4, 5, 0], 1, 2))

from typing import List


def path_existence_queries(n: int, nums: List[int], max_diff: int, queries: List[List[int]]) -> List[int]:
    sorted_nums = [(nums[i], i) for i in range(n)]
    sorted_nums.sort()

    point = [0] * n
    for i in range(n):
        point[sorted_nums[i][1]] = i

    up = [0] * (n + 1)

    j = 0
    for i in range(n):
        while j + 1 < n and sorted_nums[j + 1][0] - sorted_nums[i][0] <= max_diff:
            j += 1
        if j < i:
            j = i
        up[i] = j

    temp = n
    k = 0
    while temp:
        k += 1
        temp //= 2

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n):
        dp[i][0] = up[i]

    for col in range(1, k):
        for i in range(n):
            dp[i][col] = dp[dp[i][col - 1]][col - 1]

    result = []

    for u, v in queries:

        if u == v:
            result.append(0)
            continue

        st = min(point[u], point[v])
        en = max(point[u], point[v])

        if up[st] == st:
            result.append(-1)
            continue

        node = st
        step = 0

        for i in range(k - 1, -1, -1):
            if dp[node][i] < en:
                node = dp[node][i]
                step += 1 << i

        if up[node] < en:
            result.append(-1)
        else:
            result.append(step + 1)

    return result


print(path_existence_queries(5, [1, 8, 3, 4, 2], 3, [[0, 3], [2, 4]]))
print(path_existence_queries(5, [5, 3, 1, 9, 10], 2, [[0, 1], [0, 2], [2, 3], [4, 3]]))
print(path_existence_queries(3, [3, 6, 1], 1, [[0, 0], [0, 1], [1, 2]]))

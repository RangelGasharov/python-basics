from typing import List


def max_total_value(nums: List[int], k: int) -> int:
    n = len(nums)

    lg = [0] * (n + 1)
    for i in range(2, n + 1):
        lg[i] = lg[i // 2] + 1

    mx = [[0] * n for _ in range(lg[n] + 1)]

    mn = [[0] * n for _ in range(lg[n] + 1)]

    for i in range(n):
        mx[0][i] = nums[i]
        mn[0][i] = nums[i]

    for j in range(1, lg[n] + 1):
        length = 1 << j

        for i in range(n - length + 1):
            mx[j][i] = max(mx[j - 1][i], mx[j - 1][i + (length >> 1)])
            mn[j][i] = min(mn[j - 1][i], mn[j - 1][i + (length >> 1)])

    def get_value(l, r):
        lngth = r - l + 1
        p = lg[lngth]

        mx_val = max(mx[p][l], mx[p][r - (1 << p) + 1])

        mn_val = min(mn[p][l], mn[p][r - (1 << p) + 1])

        return mx_val - mn_val

    import heapq

    pq = []

    for l in range(n):
        heapq.heappush(pq, (-get_value(l, n - 1), l, n - 1))

    result = 0

    for _ in range(k):
        neg_val, l, r = heapq.heappop(pq)

        val = -neg_val
        result += val

        if r > l:
            heapq.heappush(pq, (-get_value(l, r - 1), l, r - 1))

    return result


print(max_total_value([1, 3, 2], 2))
print(max_total_value([4, 2, 5, 1], 3))

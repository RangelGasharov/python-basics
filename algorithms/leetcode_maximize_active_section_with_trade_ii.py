from bisect import bisect_left, bisect_right
from typing import List


def max_active_sections_after_trade(s: str, queries: List[List[int]]) -> List[int]:
    n = len(s)
    total_ones = s.count("1")

    starts, ends = [], []
    i = 0
    while i < n:
        if s[i] == "0":
            j = i
            while j < n and s[j] == "0":
                j += 1
            starts.append(i)
            ends.append(j - 1)
            i = j
        else:
            i += 1

    m = len(starts)
    full = [ends[i] - starts[i] + 1 for i in range(m)]

    P = [full[i] + full[i + 1] for i in range(m - 1)]
    Lp = len(P)
    logt = [0] * (Lp + 1)
    for x in range(2, Lp + 1):
        logt[x] = logt[x >> 1] + 1
    sparse = [P]
    k = 1
    while (1 << k) <= Lp:
        prev, half = sparse[-1], 1 << (k - 1)
        sparse.append([max(prev[i], prev[i + half]) for i in range(Lp - (1 << k) + 1)])
        k += 1

    def range_max(a, b):
        k = logt[b - a + 1]
        return max(sparse[k][a], sparse[k][b - (1 << k) + 1])

    def c_len(idx, l, r):
        return min(ends[idx], r) - max(starts[idx], l) + 1

    result = []
    for l, r in queries:
        gain = 0
        A = bisect_left(ends, l)
        B = bisect_right(starts, r) - 1
        if A < m and B >= 0 and A < B and starts[A] <= r and ends[B] >= l:
            gain = c_len(A, l, r) + c_len(A + 1, l, r)
            gain = max(gain, c_len(B - 1, l, r) + c_len(B, l, r))
            if A + 1 <= B - 2:
                gain = max(gain, range_max(A + 1, B - 2))
        result.append(total_ones + gain)
    return result



print(max_active_sections_after_trade("01", [[0, 1]]))
print(max_active_sections_after_trade("0100", [[0, 3], [0, 2], [1, 3], [2, 3]]))
print(max_active_sections_after_trade("1000100", [[1, 5], [0, 6], [0, 4]]))
print(max_active_sections_after_trade("01010", [[0, 3], [1, 4], [1, 3]]))
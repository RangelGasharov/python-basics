from operator import itemgetter
from typing import List

from numpy import inf


def count_servers(n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
    server, time = zip(*sorted(logs, key=itemgetter(1)), [0, inf])
    count = [0] * (n + 1)
    busy = lo = hi = 0
    result = [0] * len(queries)
    for i, q in sorted(enumerate(queries), key=itemgetter(1)):
        while time[hi] <= q:
            busy += not count[server[hi]]
            count[server[hi]] += 1
            hi += 1
        while time[lo] < q - x:
            count[server[lo]] -= 1
            busy -= not count[server[lo]]
            lo += 1
        result[i] = n - busy
    return result


print(count_servers(3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]))
print(count_servers(3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4]))

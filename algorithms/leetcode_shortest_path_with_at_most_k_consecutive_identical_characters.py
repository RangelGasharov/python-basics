from heapq import heappop, heappush
from typing import List


def shortest_path(n: int, edges: List[List[int]], labels: str, k: int) -> int:
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))

    best = [k + 1] * n
    heap = [(0, 1, 0)]

    while heap:
        d, run, x = heappop(heap)
        if run >= best[x]:
            continue
        if x == n - 1:
            return d
        best[x] = run
        for y, w in graph[x]:
            r = run + 1 if labels[y] == labels[x] else 1
            if r < best[y]:
                heappush(heap, (d + w, r, y))
    return -1


print(shortest_path(3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 1))
print(shortest_path(3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 2))
print(shortest_path(3, [[0, 1, 1], [1, 2, 1]], "aaa", 2))

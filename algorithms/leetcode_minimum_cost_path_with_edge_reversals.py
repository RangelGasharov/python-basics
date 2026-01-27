import heapq
import math
from collections import defaultdict


def min_cost(n: int, edges: list[list[int]]) -> int:
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, 2 * w))

    dist = [math.inf] * n
    dist[0] = 0

    heap = [(0, 0)]
    while heap:
        d, u = heapq.heappop(heap)
        if u == n - 1:
            return d
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return -1


print(min_cost(4, [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]))
print(min_cost(3, [[0, 1], [1, 2], [2, 3], [3, 0]]))

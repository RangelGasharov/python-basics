from typing import List
from collections import deque
import heapq


def maximum_safeness_factor(grid: List[List[int]]) -> int:
    n = len(grid)
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    dist = [[-1] * n for _ in range(n)]
    q = deque()
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                dist[r][c] = 0
                q.append((r, c))

    while q:
        r, c = q.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    safeness = [[-1] * n for _ in range(n)]
    heap = [(-dist[0][0], 0, 0)]
    safeness[0][0] = dist[0][0]

    while heap:
        neg_s, r, c = heapq.heappop(heap)
        s = -neg_s
        if (r, c) == (n - 1, n - 1):
            return s
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                new_s = min(s, dist[nr][nc])
                if new_s > safeness[nr][nc]:
                    safeness[nr][nc] = new_s
                    heapq.heappush(heap, (-new_s, nr, nc))

    return 0


print(maximum_safeness_factor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
print(maximum_safeness_factor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]))
print(maximum_safeness_factor([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]))

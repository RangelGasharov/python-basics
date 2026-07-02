from collections import deque
from typing import List


def find_safe_walk(grid: List[List[int]], health: int) -> bool:
    d = (0, 1, 0, -1, 0)
    rows, cols = len(grid), len(grid[0])
    n = rows * cols

    def idx(first, second):
        return first * cols + second

    max_h = [-1] * n
    q = deque()
    q.append(0)
    max_h[0] = health - grid[0][0]
    while q:
        ij = q.popleft()
        curH = max_h[ij]
        if ij == n - 1:
            return curH > 0
        i, j = divmod(ij, cols)
        for a in range(4):
            s, t = i + d[a], j + d[a + 1]
            st = idx(s, t)
            if s < 0 or s >= rows or t < 0 or t >= cols:
                continue
            H2 = curH - grid[s][t]
            if H2 > max_h[st]:
                max_h[st] = H2
                if grid[s][t] == 0:
                    q.appendleft(st)
                else:
                    q.append(st)
    return False


print(find_safe_walk([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1))
print(find_safe_walk([[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]], 3))
print(find_safe_walk([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5))

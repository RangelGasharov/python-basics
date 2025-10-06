import heapq


def swim_in_water(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    pq = [(grid[0][0], 0, 0)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    seen = set()

    while pq:
        max_d, r, c = heapq.heappop(pq)
        if (r, c) in seen: continue
        seen.add((r, c))
        if r == m - 1 and c == n - 1:
            return max_d

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                new_d = max(max_d, grid[nr][nc])
                heapq.heappush(pq, (new_d, nr, nc))

    return -1


print(swim_in_water([[0, 2], [1, 3]]))
print(swim_in_water([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))

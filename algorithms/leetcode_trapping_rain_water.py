import heapq


def trap_rain_water(height_map: list[list[int]]) -> int:
    if not height_map or not height_map[0]:
        return 0

    m, n = len(height_map), len(height_map[0])
    visited = [[False] * n for _ in range(m)]
    heap = []

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                heapq.heappush(heap, (height_map[i][j], i, j))
                visited[i][j] = True

    water = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while heap:
        height, x, y = heapq.heappop(heap)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if height_map[nx][ny] < height:
                    water += height - height_map[nx][ny]
                heapq.heappush(heap, (max(height_map[nx][ny], height), nx, ny))

    return water


print(trap_rain_water([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))
print(trap_rain_water([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
print(trap_rain_water([[19383, 10886, 12777, 16915, 17793, 18335, 15386, 10492, 16649, 11421],
                       [12362, 27, 8690, 59, 7763, 3926, 540, 3426, 9172, 5736],
                       [15211, 5368, 2567, 6429, 5782, 1530, 2862, 5123, 4067, 3135],
                       [13929, 9802, 4022, 3058, 3069, 8167, 1393, 8456, 5011, 8042],
                       [16229, 7373, 4421, 4919, 3784, 8537, 5198, 4324, 8315, 4370],
                       [16413, 3526, 6091, 8980, 9956, 1873, 6862, 9170, 6996, 7281],
                       [12305, 925, 7084, 6327, 336, 6505, 846, 1729, 1313, 5857],
                       [16124, 3895, 9582, 545, 8814, 3367, 5434, 364, 4043, 3750],
                       [11087, 6808, 7276, 7178, 5788, 3584, 5403, 2651, 2754, 2399],
                       [19932, 5060, 9676, 3368, 7739, 12, 6226, 8586, 8094, 7539]]))

from collections import deque


def latest_day_to_cross(row: int, col: int, cells: list[list[int]]) -> int:
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    state = [0] * (row * col)
    queue = deque()

    for day in range(len(cells) - 1, -1, -1):
        x, y = cells[day]
        x -= 1
        y -= 1
        idx = x * col + y

        state[idx] = 1

        if x == 0:
            state[idx] = 2
            queue.append(idx)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col:
                if state[nx * col + ny] == 2:
                    if x == row - 1:
                        return day
                    state[idx] = 2
                    queue.append(idx)
                    break

        while queue:
            cur = queue.popleft()
            cx, cy = divmod(cur, col)

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < row and 0 <= ny < col:
                    nid = nx * col + ny
                    if state[nid] == 1:
                        if nx == row - 1:
                            return day
                        state[nid] = 2
                        queue.append(nid)
    return 0


print(latest_day_to_cross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]))
print(latest_day_to_cross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]))
print(latest_day_to_cross(3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]))

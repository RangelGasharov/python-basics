from typing import List
from collections import deque


def min_moves(classroom: List[str], energy: int) -> int:
    m = len(classroom)
    n = len(classroom[0])

    id = [[-1] * n for _ in range(m)]

    k = 0
    start_row = 0
    start_col = 0

    for row in range(m):
        for col in range(n):
            if classroom[row][col] == "S":
                start_row = row
                start_col = col
            elif classroom[row][col] == "L":
                id[row][col] = k
                k += 1

    if k == 0:
        return 0

    total_mask = (1 << k) - 1

    best = [
        [[-1] * (1 << k) for _ in range(n)]
        for _ in range(m)
    ]

    queue = deque()

    max_energy = energy

    best[start_row][start_col][0] = energy
    queue.append((start_row, start_col, 0, energy, 0))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col, mask, energy, moves = queue.popleft()

        for dir_row, dir_col in directions:
            new_rol = row + dir_row
            new_col = col + dir_col

            if new_rol < 0 or new_rol >= m or new_col < 0 or new_col >= n or classroom[new_rol][new_col] == "X":
                continue

            new_energy = energy - 1

            if new_energy < 0:
                continue

            new_mask = mask

            if classroom[new_rol][new_col] == "L":
                new_mask |= 1 << id[new_rol][new_col]

            if classroom[new_rol][new_col] == "R":
                new_energy = max_energy

            if new_mask == total_mask:
                return moves + 1

            if new_energy <= best[new_rol][new_col][new_mask]:
                continue

            best[new_rol][new_col][new_mask] = new_energy

            queue.append((new_rol, new_col, new_mask, new_energy, moves + 1))

    return -1


print(min_moves(["S.", "XL"], 2))
print(min_moves(["LS", "RL"], 4))
print(min_moves(["L.S", "RXL"], 3))
print(min_moves(["RL", "SL", "LR"], 2))

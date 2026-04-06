from typing import List


def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
    blocked = set()
    for o in obstacles:
        blocked.add((o[0], o[1]))

    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0)
    ]

    x, y = 0, 0
    direction = 0
    max_dist = 0

    for cmd in commands:
        if cmd == -1:
            direction = (direction + 1) % 4
        elif cmd == -2:
            direction = (direction + 3) % 4
        else:
            while cmd > 0:
                nx = x + directions[direction][0]
                ny = y + directions[direction][1]

                if (nx, ny) in blocked:
                    break

                x = nx
                y = ny

                max_dist = max(max_dist, x * x + y * y)
                cmd -= 1
    return max_dist


print(robotSim([4, -1, 3], []))
print(robotSim([4, -1, 4, -2, 4], [[2, 4]]))
print(robotSim([6, -1, -1, 6], [[0, 0]]))

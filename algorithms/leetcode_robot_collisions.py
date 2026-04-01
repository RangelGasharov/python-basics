from typing import List


def survivedRobotsHealths(positions: List[int], healths: List[int], directions: str) -> List[int]:
    n = len(positions)
    order = sorted(range(n), key=lambda index: positions[index])
    dead = [False] * n
    stk = []

    for i in order:
        if directions[i] == "R":
            stk.append(i)
        else:
            while stk and directions[stk[-1]] == "R":
                top = stk[-1]
                if healths[top] > healths[i]:
                    healths[top] -= 1
                    dead[i] = True
                    break
                elif healths[top] < healths[i]:
                    healths[i] -= 1
                    dead[top] = True
                    stk.pop()
                else:
                    dead[i] = dead[top] = True
                    stk.pop()
                    break
            if not dead[i]:
                stk.append(i)

    return [healths[i] for i in range(n) if not dead[i]]


print(survivedRobotsHealths([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR"))
print(survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], "RLRL"))
print(survivedRobotsHealths([1, 2, 5, 6], [10, 10, 11, 11], "RLRL"))

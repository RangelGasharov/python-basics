from typing import List


def max_number_of_families(n: int, reserved_seats: List[List[int]]) -> int:
    LEFT, MID, RIGHT = 0b111100, 0b11110000, 0b1111000000

    rows = {}
    for row, col in reserved_seats:
        rows[row] = rows.get(row, 0) | (1 << col)

    result = 2 * (n - len(rows))

    for mask in rows.values():
        left = not (mask & LEFT)
        right = not (mask & RIGHT)
        if left and right:
            result += 2
        elif left or right or not (mask & MID):
            result += 1

    return result


print(max_number_of_families(3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
print(max_number_of_families(2, [[2, 1], [1, 8], [2, 6]]))
print(max_number_of_families(4, [[4, 3], [1, 4], [4, 6], [1, 7]]))

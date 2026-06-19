from typing import List


def largest_altitude(gain: List[int]) -> int:
    current = 0
    max_lat = 0
    for i in range(len(gain)):
        current += gain[i]
        if current > max_lat:
            max_lat = current
    return max_lat


print(largest_altitude([-5, 1, 5, 0, -7]))
print(largest_altitude([-4, -3, -2, -1, 4, 3, 2]))
print(largest_altitude([1, 4, 3, 2, 1]))

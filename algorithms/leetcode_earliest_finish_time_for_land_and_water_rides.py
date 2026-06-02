from typing import List


def earliest_finish_time(land_start_time: List[int], land_duration: List[int], water_start_time: List[int],
                         water_duration: List[int]) -> int:
    min_l, min_w, result = float("inf"), float("inf"), float("inf")
    n = len(land_start_time)
    m = len(water_start_time)

    for i in range(n):
        min_l = min(min_l, land_start_time[i] + land_duration[i])

    for i in range(m):
        min_w = min(min_w, water_start_time[i] + water_duration[i])
        result = min(result, max(min_l, water_start_time[i]) + water_duration[i])

    for i in range(n):
        result = min(result, max(min_w, land_start_time[i]) + land_duration[i])

    return result


print(earliest_finish_time([2, 8], [4, 1], [6], [3]))
print(earliest_finish_time([5], [3], [1], [10]))

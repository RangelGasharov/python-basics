def earliest_finish_time(land_start_time: list[int], land_duration: list[int], water_start_time: list[int],
                         water_duration: list[int]) -> int:
    l = w = min_l = min_w = float("inf")
    n, m = len(land_start_time), len(water_start_time)

    for i in range(n):
        l = min(l, land_start_time[i] + land_duration[i])

    for i in range(m):
        w = min(w, water_start_time[i] + water_duration[i])
        min_l = min(min_l, max(water_start_time[i], l) + water_duration[i])

    for i in range(n):
        min_w = min(min_w, max(land_start_time[i], w) + land_duration[i])

    return min(min_w, min_l)


print(earliest_finish_time([2, 8], [4, 1], [6], [3]))
print(earliest_finish_time([5], [3], [1], [10]))

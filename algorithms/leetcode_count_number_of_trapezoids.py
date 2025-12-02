from math import comb


def count_trapezoids(points: list[list[int]]) -> int:
    mod = int(10 ** 9 + 7)
    result = 0
    prefix_sum = 0

    freq_dict = dict()

    for point in points:
        if point[1] not in freq_dict:
            freq_dict[point[1]] = 1
        else:
            freq_dict[point[1]] += 1

    for y, freq in freq_dict.items():
        freq_dict[y] = comb(freq, 2)

    for e in freq_dict.values():
        result = (result + e * prefix_sum) % mod
        prefix_sum = (prefix_sum + e) % mod

    return result


print(count_trapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))
print(count_trapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]))

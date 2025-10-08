from bisect import bisect_left


def successful_pairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    potions.sort()
    n = len(potions)
    result = []

    for spell in spells:
        lowest_multiple = success / spell
        index = bisect_left(potions, lowest_multiple)
        result.append(n - index)
    return result


print(successful_pairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
print(successful_pairs([3, 1, 2], [8, 5, 8], 16))

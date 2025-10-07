from sortedcontainers import SortedList


def avoid_flood(rains: list[int]) -> list[int]:
    res, full, dry = [-1] * len(rains), {}, SortedList()
    for i, lake in enumerate(rains):
        if lake == 0:
            dry.add(i)
            res[i] = 1
        elif lake in full:
            j = dry.bisect_right(full[lake])
            if j == len(dry):
                return []
            res[dry[j]] = lake
            dry.pop(j)
            full[lake] = i
        else:
            full[lake] = i
    return res


print(avoid_flood([1, 2, 3, 4]))
print(avoid_flood([1, 2, 0, 0, 2, 1]))
print(avoid_flood([1, 2, 0, 1, 2]))
print(avoid_flood([1, 1, 1, 0, 0]))

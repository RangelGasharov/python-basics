from heapq import heappush, heappop
from statistics import multimode


def busiest_servers(k: int, arrival: list[int], load: list[int]) -> list[int]:
    free = list(range(k))

    handled, busy = [], []
    for i, (t, d) in enumerate(zip(arrival, load)):
        while busy and busy[0][0] <= t:
            heappush(free, i + (heappop(busy)[1] - i) % k)
        if free:
            x = heappop(free) % k
            heappush(busy, (t + d, x))
            handled.append(x)

    return multimode(handled)

print(busiest_servers(3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3]))
print(busiest_servers(3, [1, 2, 3, 4], [1, 2, 1, 2]))
print(busiest_servers(3, [1, 2, 3], [10, 12, 11]))
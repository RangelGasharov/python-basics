import heapq


def assign_tasks(servers: list[int], tasks: list[int]) -> list[int]:
    n = len(servers)
    m = len(tasks)
    result = [0] * m

    available = [(servers[i], i) for i in range(n)]
    heapq.heapify(available)
    busy = []

    for i in range(m):
        while busy and busy[0][0] <= i:
            free_time, server = heapq.heappop(busy)
            heapq.heappush(available, server)
        if available:
            weight, index = heapq.heappop(available)
            result[i] = index
            heapq.heappush(busy, (i + tasks[i], (weight, index)))
        else:
            free_time, server = heapq.heappop(busy)
            weight, index = server
            result[i] = index
            heapq.heappush(busy, (free_time + tasks[i], server))
    return result


print(assign_tasks([3, 3, 2], [1, 2, 3, 2, 1, 2]))
print(assign_tasks([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1]))

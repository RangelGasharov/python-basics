import heapq


def most_booked(n, meetings):
    free = list(range(n))
    heapq.heapify(free)
    busy = []
    count = [0] * n

    meetings.sort()

    for start, end in meetings:
        duration = end - start

        while busy and busy[0][0] <= start:
            _, room = heapq.heappop(busy)
            heapq.heappush(free, room)

        if free:
            room = heapq.heappop(free)
            heapq.heappush(busy, (end, room))
            count[room] += 1
        else:
            time, room = heapq.heappop(busy)
            heapq.heappush(busy, (time + duration, room))
            count[room] += 1

    return count.index(max(count))


print(most_booked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))
print(most_booked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))

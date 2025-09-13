import heapq


def max_average_ratio(classes, new_students):
    def gain(a, b):
        return float(a + 1) / (b + 1) - float(a) / b

    heap = [(-gain(a, b), a, b) for a, b in classes]
    heapq.heapify(heap)

    for _ in range(new_students):
        g, a, b = heapq.heappop(heap)
        a += 1
        b += 1
        heapq.heappush(heap, (-gain(a, b), a, b))

    return sum(float(a) / b for _, a, b in heap) / len(heap)


print(max_average_ratio([[1, 2], [3, 5], [2, 2]], 2))
print(max_average_ratio([[2, 4], [3, 9], [4, 5], [2, 10]], 4))
print(max_average_ratio([[376, 562], [720, 904], [691, 795], [384, 756], [89, 450], [521, 680]], 5))
print(max_average_ratio([[583, 868], [783, 822], [65, 262], [121, 508], [461, 780], [484, 668]], 8))

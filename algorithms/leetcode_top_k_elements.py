import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counter = {}
    heap = []
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    for key, value in counter.items():
        heapq.heappush(heap, (-value, key))

    result = []
    while len(result) < k:
        result.append(heapq.heappop(heap)[1])
    return result


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print(top_k_frequent([1], 1))
print(top_k_frequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
print(top_k_frequent([2, 2, 2, 2, 2, 3, 1, 1, 1], 2))

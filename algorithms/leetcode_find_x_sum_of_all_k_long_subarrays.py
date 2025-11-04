import heapq


def find_x_sum(nums: list[int], k: int, x: int) -> list[int]:
    result = []
    n = len(nums)
    counter = {}

    def sum_of_k_most_frequent_elements() -> int:
        heap = []
        for key, value in counter.items():
            heapq.heappush(heap, (-value, -key))
        sum_most_frequent = 0
        for _ in range(min(x, len(heap))):
            freq, neg_key = heapq.heappop(heap)
            num = -neg_key
            sum_most_frequent += num * counter[num]
        return sum_most_frequent

    for i in range(0, k):
        if nums[i] in counter:
            counter[nums[i]] += 1
        else:
            counter[nums[i]] = 1

    for i in range(0, n - k + 1):
        result.append(sum_of_k_most_frequent_elements())
        counter[nums[i]] -= 1
        if counter[nums[i]] == 0:
            del counter[nums[i]]
        if i + k < n:
            counter[nums[i + k]] = counter.get(nums[i + k], 0) + 1
    return result


print(find_x_sum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2))
print(find_x_sum(
    [25, 26, 27, 28, 29, 30, 19, 18, 17, 16, 15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 25, 26, 27, 28, 29, 30,
     19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 25, 25))

def count_partitions(nums: list[int]) -> int:
    if sum(nums) % 2 == 0:
        return len(nums) - 1
    return 0


print(count_partitions([10, 10, 3, 7, 6]))
print(count_partitions([1, 2, 2]))
print(count_partitions([2, 4, 6, 8]))

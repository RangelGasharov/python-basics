def special_triplets(nums: list[int]) -> int:
    mod = 10 ** 9 + 7
    n = len(nums)
    result = 0
    total_freq = {}

    for x in nums:
        total_freq[x] = total_freq.get(x, 0) + 1

    count_zero = total_freq.get(0, 0)

    result += int(((count_zero * (count_zero - 1) * (count_zero - 2)) / 6)) % mod

    prefix = {}
    suffix = total_freq.copy()

    for j in range(n):
        x = nums[j]

        suffix[x] -= 1
        if suffix[x] == 0:
            del suffix[x]

        if j == 0 or j == n - 1:
            prefix[x] = prefix.get(x, 0) + 1
            continue

        if x != 0:
            target = 2 * x

            freq_1 = prefix.get(target, 0)
            freq_2 = suffix.get(target, 0)

            result = (result + freq_1 * freq_2) % mod

        prefix[x] = prefix.get(x, 0) + 1

    return result % mod


print(special_triplets([6, 3, 6]))
print(special_triplets([0, 1, 0, 0]))
print(special_triplets([8, 4, 2, 8, 4]))
print(special_triplets([0, 0, 0, 0, 0, 0, 0, 0, 0]))

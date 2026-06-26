def count_majority_subarrays(nums, target):
    n = len(nums)
    count = 0

    for i in range(n):
        if nums[i] == target:
            nums[i] = 1
        else:
            nums[i] = -1

    pref = [0] * n
    pref[0] = nums[0]

    for i in range(1, n):
        pref[i] = pref[i - 1] + nums[i]

    shift = n
    freq = [0] * (2 * n + 1)

    freq[shift] = 1

    valid = 0
    last_sum = 0

    for i in range(n):
        if pref[i] > last_sum:
            valid += freq[last_sum + shift]
        else:
            valid -= freq[pref[i] + shift]

        count += valid
        freq[pref[i] + shift] += 1
        last_sum = pref[i]

    return count


print(count_majority_subarrays([1, 2, 2, 3], 2))
print(count_majority_subarrays([1, 1, 1, 1], 1))
print(count_majority_subarrays([1, 2, 3], 4))

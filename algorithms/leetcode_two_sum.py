def two_sum(nums, target):
    if len(nums) == 0:
        return []
    seen = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in seen:
            return [seen[difference], i]
        else:
            seen[nums[i]] = i
    return []
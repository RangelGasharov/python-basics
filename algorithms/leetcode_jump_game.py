def jump_game(nums):
    n = len(nums)
    goal = n - 1

    for i in range(n - 1, -1, -1):
        max_jump = nums[i]
        if i + max_jump >= goal:
            goal = i

    if goal == 0:
        return True
    else:
        return False


print(jump_game([2, 3, 1, 1, 4]))
print(jump_game([3, 2, 1, 0, 4]))
print(jump_game([3, 2, 1, 1, 4]))
print(jump_game([4, 3, 2, 1, 6]))
print(jump_game([1, 1, 100]))

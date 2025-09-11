def get_permutations(nums):
    if len(nums) == 0:
        return []

    answer, solution = [], []

    def backtrack():
        if len(solution) == len(nums):
            answer.append(solution[:])
            return

        for num in nums:
            if num not in solution:
                solution.append(num)
                backtrack()
                solution.pop()

    backtrack()
    return answer


print(get_permutations([0]))
print(get_permutations([0, 1]))
print(get_permutations([1, 2, 3]))
print(get_permutations([1, 2, 3, 4]))

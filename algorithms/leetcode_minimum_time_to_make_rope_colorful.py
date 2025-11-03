def minCost(colors: str, neededTime: list[int]) -> int:
    total_time = 0
    current_sum = neededTime[0]
    current_max = neededTime[0]

    for i in range(1, len(colors)):
        if colors[i] == colors[i - 1]:
            current_sum += neededTime[i]
            current_max = max(current_max, neededTime[i])
        else:
            total_time += current_sum - current_max
            current_sum = neededTime[i]
            current_max = neededTime[i]
    total_time += current_sum - current_max
    return total_time


print(minCost("abc", [1, 1, 1]))
print(minCost("abb", [1, 1, 1]))
print(minCost("abaac", [1, 2, 3, 4, 5]))
print(minCost("aabaa", [1, 2, 3, 4, 1]))
print(minCost("cddcdcae", [4, 8, 8, 4, 4, 5, 4, 2]))
print(minCost("abbaaccbaaa", [1, 2, 3, 4, 1, 1, 2, 3, 4, 2, 2]))
print(minCost("bbbaaa", [4, 9, 3, 8, 8, 9]))

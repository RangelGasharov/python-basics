def getDescentPeriods(prices: list[int]) -> int:
    n = len(prices)
    result = 0
    streak = 0

    for i in range(n):
        if i > 0 and prices[i] == prices[i - 1] - 1:
            streak += 1
        else:
            streak = 1
        result += streak

    return result


print(getDescentPeriods([1, 3, 5, 7, 9]))
print(getDescentPeriods([3, 2, 1, 4]))
print(getDescentPeriods([8, 6, 7, 7]))
print(getDescentPeriods([1]))

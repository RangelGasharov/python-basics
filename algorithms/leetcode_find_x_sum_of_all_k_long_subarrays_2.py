from collections import Counter

from sortedcontainers import SortedList


def find_x_sum(nums: list[int], k: int, x: int) -> list[int]:
    n = len(nums)
    counter = Counter()
    result = []

    top = SortedList()
    rest = SortedList()
    top_sum = 0

    def add(num):
        nonlocal top_sum
        old_freq = counter[num]
        if old_freq > 0:
            entry = (-old_freq, -num)
            if entry in top:
                top.remove(entry)
                top_sum -= num * old_freq
            else:
                rest.remove(entry)
        counter[num] += 1
        new_entry = (-counter[num], -num)
        rest.add(new_entry)
        rebalance()

    def remove(num):
        nonlocal top_sum
        old_freq = counter[num]
        entry = (-old_freq, -num)
        if entry in top:
            top.remove(entry)
            top_sum -= num * old_freq
        else:
            rest.remove(entry)
        counter[num] -= 1
        if counter[num] > 0:
            new_entry = (-counter[num], -num)
            rest.add(new_entry)
        rebalance()

    def rebalance():
        nonlocal top_sum
        while len(top) < x and rest:
            freq_val, neg_num = rest.pop(0)
            num = -neg_num
            top.add((freq_val, neg_num))
            top_sum += num * (-freq_val)
        while len(top) > x:
            freq_val, neg_num = top.pop()
            num = -neg_num
            top_sum -= num * (-freq_val)
            rest.add((freq_val, neg_num))
        while rest and top and rest[0] < top[-1]:
            f1, n1 = rest.pop(0)
            f2, n2 = top.pop()
            num1, num2 = -n1, -n2
            top_sum -= num2 * (-f2)
            top_sum += num1 * (-f1)
            top.add((f1, n1))
            rest.add((f2, n2))

    for i in range(k):
        add(nums[i])
    result.append(top_sum)

    for i in range(k, n):
        add(nums[i])
        remove(nums[i - k])
        result.append(top_sum)

    return result


print(find_x_sum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2))
print(find_x_sum(
    [25, 26, 27, 28, 29, 30, 19, 18, 17, 16, 15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 25, 26, 27, 28, 29, 30,
     19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 25, 25))

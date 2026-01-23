from sortedcontainers import SortedList


def minimum_pair_removal(nums: list[int]) -> int:
    n = len(nums)
    if n < 2:
        return 0

    array = [int(x) for x in nums]
    left = list(range(-1, n - 1))
    right = list(range(1, n + 1))

    flipped = 0
    pair_sum = SortedList()


    def add(i, n, array):
        nonlocal flipped
        if 0 <= i < n:
            j = right[i]
            if j < n:
                pair_sum.add([array[i] + array[j], i])
                if array[i] > array[j]:
                    flipped += 1


    def remove(i, n, array):
        nonlocal flipped
        if 0 <= i < n:
            j = right[i]
            if j < n:
                if array[i] > array[j]:
                    flipped -= 1
                pair_sum.discard([array[i] + array[j], i])


    for i in range(n - 1):
        if array[i] > array[i + 1]:
            flipped += 1
        pair_sum.add([array[i] + array[i + 1], i])

    op = 0

    while flipped > 0 and pair_sum:
        s, i = pair_sum.pop(0)

        j = right[i]
        h = left[i]
        k = right[j]

        remove(h, n, array)
        if array[i] > array[j]:
            flipped -= 1
        remove(j, n, array)

        array[i] += array[j]
        op += 1

        right[i] = k
        if k < n:
            left[k] = i

        add(h, n, array)
        add(i, n, array)

    return op


print(minimum_pair_removal([5,2,3,1]))
print(minimum_pair_removal([1,2,2]))
def result_array(nums, k, queries):
    n = 1

    while n < len(nums):
        n <<= 1

    count = [[0] * k for _ in range(2 * n)]
    prod = [1] * (2 * n)

    for i in range(len(nums)):
        r = nums[i] % k
        count[n + i][r] = 1
        prod[n + i] = r

    def merge(i):
        l = i * 2
        r = l + 1

        a = count[l]
        b = count[r]
        c = count[i]

        for x in range(k):
            c[x] = a[x]

        for x in range(k):
            if b[x]:
                y = (prod[l] * x) % k
                c[y] += b[x]

        prod[i] = (prod[l] * prod[r]) % k

    for i in range(n - 1, 0, -1):
        merge(i)

    def update(index, value):
        pos = n + index
        value %= k

        current = count[pos]

        for x in range(k):
            current[x] = 0

        current[value] = 1
        prod[pos] = value

        pos //= 2

        while pos:
            merge(pos)
            pos //= 2

    def query(l, r):
        a = [0] * k
        b = [0] * k

        ap = 1
        bp = 1

        l += n
        r += n

        while l < r:
            if l & 1:
                base = count[l]
                temp = a[:]

                for x in range(k):
                    if base[x]:
                        y = (ap * x) % k
                        temp[y] += base[x]

                a = temp
                ap = (ap * prod[l]) % k
                l += 1

            if r & 1:
                r -= 1

                base = count[r]
                temp = [0] * k

                for x in range(k):
                    temp[x] = base[x]

                for x in range(k):
                    if b[x]:
                        y = (prod[r] * x) % k
                        temp[y] += b[x]

                b = temp
                bp = (prod[r] * bp) % k

            l //= 2
            r //= 2

        result = a[:]

        for x in range(k):
            if b[x]:
                y = (ap * x) % k
                result[y] += b[x]

        return result

    result = []

    for index, value, start, x in queries:
        update(index, value)

        current = query(start, len(nums))
        result.append(current[x])

    return result


print(result_array([1, 2, 3, 4, 5], 3, [[2, 2, 0, 2], [3, 3, 3, 0], [0, 1, 0, 1]]))
print(result_array([1, 2, 4, 8, 16, 32], 4, [[0, 2, 0, 2], [0, 2, 0, 1]]))
print(result_array([1, 1, 2, 1, 1], 2, [[2, 1, 0, 1]]))

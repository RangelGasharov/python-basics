class Solution:
    mod = 1000000007

    def mod_exp(self, base, exp):
        if exp == 0:
            return 1

        half = self.mod_exp(base, exp // 2)
        result = (half * half) % self.mod

        if exp % 2:
            result = (result * base) % self.mod

        return result

    def xor_after_queries(self, arr, ops):
        n = len(arr)
        block = int(n ** 0.5) + 1

        buckets = [[] for _ in range(block)]

        for query in ops:
            left, right, step, val = query

            if step < block:
                buckets[step].append(query)
            else:
                pos = left
                while pos <= right:
                    arr[pos] = (arr[pos] * val) % self.mod
                    pos += step

        for step in range(1, block):
            if not buckets[step]:
                continue

            multiplier = [1] * (n + step + 5)

            for query in buckets[step]:
                left, right, _, val = query

                last_index = left + ((right - left) // step) * step
                stop = last_index + step

                multiplier[left] = (multiplier[left] * val) % self.mod

                inv_val = self.mod_exp(val, self.mod - 2)
                multiplier[stop] = (multiplier[stop] * inv_val) % self.mod

            for i in range(n):
                if i - step >= 0:
                    multiplier[i] = (multiplier[i] * multiplier[i - step]) % self.mod

            for i in range(n):
                arr[i] = (arr[i] * multiplier[i]) % self.mod

        result = 0
        for value in arr:
            result ^= value

        return result


solution = Solution()
print(solution.xor_after_queries([1, 1, 1], [[0, 2, 1, 4]]))
print(solution.xor_after_queries([2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]]))

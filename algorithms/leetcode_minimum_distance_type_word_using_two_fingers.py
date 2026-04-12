class Solution:
    def cal(self, a, b):
        return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

    def minimum_distance(self, word):
        n = len(word)
        dp = [0] * 26
        ndp = [0] * 26

        for i in range(1, n):
            p = ord(word[i - 1]) - ord("A")
            t = ord(word[i]) - ord("A")

            for j in range(26):
                ndp[j] = dp[j] + self.cal(p, t)

            for j in range(26):
                ndp[p] = min(ndp[p], dp[j] + self.cal(j, t))

            dp, ndp = ndp, dp

        return min(dp)


solution = Solution()
print(solution.minimum_distance("ABCD"))
print(solution.minimum_distance("CAKE"))
print(solution.minimum_distance("HAPPY"))
print(solution.minimum_distance("HELLO"))

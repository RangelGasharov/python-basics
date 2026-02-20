class Solution:
    def make_largest_special(self, s: str) -> str:
        count = 0
        i = 0
        res = []

        for j in range(len(s)):
            count += 1 if s[j] == "1" else -1

            if count == 0:
                res.append("1" + self.make_largest_special(s[i + 1:j]) + "0")
                i = j + 1

        res.sort(reverse=True)
        return "".join(res)


sol = Solution()
print(sol.make_largest_special(""))
print(sol.make_largest_special("11011000"))
print(sol.make_largest_special("10"))

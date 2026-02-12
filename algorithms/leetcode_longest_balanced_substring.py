class Solution:
    def longest_balanced(self, s: str) -> int:
        count = 1
        n = len(s)
        for l in range(n):
            freq = [0] * 26
            uniq, max_f, count_max = 0, 0, 0
            for r in range(l, n):
                freq[ord(s[r]) - 97] += 1
                f = freq[ord(s[r]) - 97]
                uniq += f == 1
                if f > max_f:
                    max_f = f
                    count_max = 1
                elif f == max_f:
                    count_max += 1
                if uniq == count_max:
                    count = max(count, r - l + 1)
        return count

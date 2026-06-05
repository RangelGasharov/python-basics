class Solution:
    waves = []
    for i in range(1000):
        r = i % 10
        m = (i // 10) % 10
        l = (i // 100) % 10
        if (m > max(l, r)) | (m < min(l, r)):
            waves.append(i)

    def total_waviness(self, num1: int, num2: int) -> int:
        return self.wave_count(num2) - self.wave_count(num1 - 1)

    def wave_count(self, num):
        if num < 100: return 0
        return sum(self.count_ways(num, p) for p in self.waves)

    def count_ways(self, num, pattern):
        s = str(num)
        n = len(s)
        t = pattern < 100
        count = 0
        for i in range(n - 2):
            pre = int(s[:i] or 0)
            cur = int(s[i:i + 3])
            suf = int(s[i + 3:] or 0)
            mult = 10 ** (n - i - 3)
            ways = 0

            if cur > pattern:
                ways = pre - t + 1
            elif cur == pattern:
                ways = max(0, pre - t)
                count += suf + 1
            else:
                ways = max(0, pre - t)
            count += ways * mult

        return count


print(Solution().total_waviness(120, 2032728182))

def number_of_substrings(s: str) -> int:
    n = len(s)
    dp = [-1] * (n + 1)
    for i in range(n):
        if i == 0 or s[i - 1] == '0':
            dp[i + 1] = i
        else:
            dp[i + 1] = dp[i]
    result = 0
    for i in range(1, n + 1):
        cnt0 = 1 if s[i - 1] == '0' else 0
        j = i
        while j > 0 and cnt0 * cnt0 <= n:
            cnt1 = (i - dp[j]) - cnt0
            if cnt0 * cnt0 <= cnt1:
                result += min(j - dp[j], cnt1 - cnt0 * cnt0 + 1)
            j = dp[j]
            cnt0 += 1
    return result


print(number_of_substrings("0001"))
print(number_of_substrings("0111"))
print(number_of_substrings("0101011"))

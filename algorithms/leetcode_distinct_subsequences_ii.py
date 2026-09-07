def distinct_subseq_ii(s: str) -> int:
    MOD = 10 ** 9 + 7
    total = 0
    dp = [0] * 26

    for char in s:
        char = ord(char) - 97
        new = total + 1 - dp[char]
        total = (total + new) % MOD
        dp[char] = (dp[char] + new) % MOD

    return total

print(distinct_subseq_ii("abc"))
print(distinct_subseq_ii("aba"))
print(distinct_subseq_ii("aaa"))
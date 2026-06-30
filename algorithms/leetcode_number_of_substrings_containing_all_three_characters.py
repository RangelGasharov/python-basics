def number_of_substrings(s: str) -> int:
    res = 0
    p = [50_000, -1, -1, -1]

    for i, ch in enumerate(s):
        p[ord(ch) & 31] = i
        res += min(p) + 1

    return res


print(number_of_substrings("abcabc"))
print(number_of_substrings("aaacb"))
print(number_of_substrings("abc"))
print(number_of_substrings("abcabcbb"))

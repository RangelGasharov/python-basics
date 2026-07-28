from typing import Counter


def smallest_palindrome(s: str) -> str:
    n = len(s)
    count = Counter(s[:n // 2])
    first = "".join(ch * count[ch] for ch in "abcdefghijklmnopqrstuvwxyz")
    mid = s[n // 2] if n & 1 else ""
    return first + mid + first[::-1]


print(smallest_palindrome("daccad"))
print(smallest_palindrome("babab"))
print(smallest_palindrome("baaab"))
print(smallest_palindrome("z"))

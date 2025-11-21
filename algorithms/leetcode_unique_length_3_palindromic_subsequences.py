def count_palindromic_subsequence(s: str) -> int:
    if len(s) <= 2:
        return 0

    chars = set(s)
    result = 0
    for char in chars:
        first = s.find(char)
        last = s.rfind(char)

        if first != last:
            result += len(set(s[first + 1:last]))

    return result


print(count_palindromic_subsequence("aabca"))
print(count_palindromic_subsequence("adc"))
print(count_palindromic_subsequence("bbcbaba"))

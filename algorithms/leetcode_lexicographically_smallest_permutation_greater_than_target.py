def lex_greater_permutation(s: str, target: str) -> str:
    freq = {}
    result = ""

    for letter in s:
        freq[letter] = freq.get(letter, 0) + 1

    for i in range(len(target)):
        if not freq.get(target[i], 0):
            break
        result += target[i]
        freq[target[i]] -= 1

    start_index = min(len(result), len(target) - 1)

    for i in range(start_index, -1, -1):
        if i < len(result):
            last = result[i]
            result = result[:-1]
            freq[last] += 1

        for letter in "abcdefghijklmnopqrstuvwxyz":
            if freq.get(letter, 0) and letter > target[i]:
                result += letter
                freq[letter] -= 1

                for l in "abcdefghijklmnopqrstuvwxyz":
                    result += freq.get(l, 0) * l
                    freq[l] = 0

                return result

    return ""


print(lex_greater_permutation("abc", "bba"))
print(lex_greater_permutation("leet", "code"))
print(lex_greater_permutation("baba", "bbaa"))

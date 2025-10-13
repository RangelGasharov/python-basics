def remove_anagrams(words: list[str]) -> list[str]:
    result = []
    for w in words:
        if not result or sorted(result[-1]) != sorted(w):
            result.append(w)
    return result


print(remove_anagrams(["abba", "baba", "bbaa", "cd", "cd"]))
print(remove_anagrams(["a", "b", "c", "d", "e"]))
print(remove_anagrams(["a", "z", "z", "z", "b", "a"]))

def max_frequency_sum(s):
    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    consonants = {}
    for letter in s:
        if letter in vowels:
            vowels[letter] += 1
        else:
            if letter in consonants:
                consonants[letter] += 1
            else:
                consonants[letter] = 1
    return (max(vowels.values()) if vowels else 0) + (max(consonants.values()) if consonants else 0)


print(max_frequency_sum("successes"))
print(max_frequency_sum("aeiaeia"))

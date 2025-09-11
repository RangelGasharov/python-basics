def sort_vowels(text):
    if len(text) == 0:
        return ""

    result = []
    vowels = "AEIOUaeiou"
    vowels_dictionary = {vowel: 0 for vowel in vowels}

    for char in text:
        if char in vowels:
            vowels_dictionary[char] += 1

    vowel_ptr = 0
    for char in text:
        if char not in vowels_dictionary:
            result.append(char)
        else:
            while vowel_ptr < len(vowels) and vowels_dictionary[vowels[vowel_ptr]] == 0:
                vowel_ptr += 1
            result.append(vowels[vowel_ptr])
            vowels_dictionary[vowels[vowel_ptr]] -= 1

    return "".join(result)


print(sort_vowels("lEetcOde"))
print(sort_vowels("lYmpH"))
print(sort_vowels(""))

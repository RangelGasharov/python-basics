def number_of_special_chars(word: str) -> int:
    first_upper = {}
    last_lower = {}

    count = 0
    for i, letter in enumerate(word):
        if letter.isupper():
            if letter not in first_upper:
                first_upper[letter] = i
        else:
            last_lower[letter] = i

    for letter, index in first_upper.items():

        if letter.lower() not in last_lower:
            continue
        if last_lower[letter.lower()] < index:
            count += 1
    return count


print(number_of_special_chars("aaAbcBC"))
print(number_of_special_chars("abc"))
print(number_of_special_chars("abBCab"))
print(number_of_special_chars("aAA"))
print(number_of_special_chars("AAa"))

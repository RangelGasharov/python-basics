def number_of_special_chars(word: str) -> int:
    seen = set()
    done = set()
    count = 0
    for letter in word:
        if letter not in seen:
            seen.add(letter)
        if letter.islower():
            if letter.upper() in seen and letter not in done:
                count += 1
                done.add(letter)
                done.add(letter.upper())
        elif letter.isupper():
            if letter.lower() in seen and letter not in done:
                count += 1
                done.add(letter)
                done.add(letter.upper())

    return count


print(number_of_special_chars("aaAbcBC"))
print(number_of_special_chars("abc"))
print(number_of_special_chars("abBCab"))
print(number_of_special_chars("aAA"))

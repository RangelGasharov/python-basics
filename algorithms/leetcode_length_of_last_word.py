def length_of_last_word(s: str) -> int:
    n = len(s)
    word_len = 0
    is_valid = False
    for i in range(n - 1, -1, -1):
        if s[i] != " ":
            is_valid = True
            word_len += 1
        if s[i] == " " and is_valid:
            return word_len
    return word_len


print(length_of_last_word("Hello World"))
print(length_of_last_word("   fly me   to   the moon  "))
print(length_of_last_word("luffy is still joyboy"))
print(length_of_last_word(" a a"))
print(length_of_last_word(" a "))

def can_be_typed_words(text, broken_letters):
    if len(text) == 0:
        return 0
    words = text.split(" ")
    amount_of_words = len(words)
    for word in words:
        for char in word:
            if char in broken_letters:
                amount_of_words -= 1
                break
    return amount_of_words


print(can_be_typed_words("hello world", "ad"))
print(can_be_typed_words("leet code", "lt"))
print(can_be_typed_words("leet code", "e"))
print(can_be_typed_words("", ""))

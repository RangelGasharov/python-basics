def decode_ciphertext(encoded_text: str, rows: int) -> str:
    if rows == 1:
        return encoded_text

    n = len(encoded_text)
    cols = n // rows
    i, j, k = 0, 0, 0
    original_text = []

    while k < n:
        original_text.append(encoded_text[k])
        i += 1
        if i == rows:
            i = 0
            j += 1
        k = i * (cols + 1) + j

    return "".join(original_text).rstrip()


print(decode_ciphertext("ch   ie   pr", 3))
print(decode_ciphertext("iveo    eed   l te   olc", 4))
print(decode_ciphertext("coding", 1))

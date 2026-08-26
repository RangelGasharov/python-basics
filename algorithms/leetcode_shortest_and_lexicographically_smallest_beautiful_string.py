def shortest_beautiful_substring(s: str, k: int) -> str:
    current_shortest = ""
    num_of_ones = 0
    min_length = float("inf")

    left = 0

    for right in range(len(s)):
        if s[right] == "1":
            num_of_ones += 1

        while num_of_ones >= k:
            current_string = s[left:right + 1]
            current_length = right - left + 1

            if current_length < min_length:
                min_length = current_length
                current_shortest = current_string
            elif current_length == min_length and current_string < current_shortest:
                current_shortest = current_string

            if s[left] == "1":
                num_of_ones -= 1

            left += 1

    return current_shortest


print(shortest_beautiful_substring("101010101", 3))
print(shortest_beautiful_substring("100011001", 3))
print(shortest_beautiful_substring("1011", 3))
print(shortest_beautiful_substring("1011", 2))
print(shortest_beautiful_substring("1011", 4))
print(shortest_beautiful_substring("000", 1))

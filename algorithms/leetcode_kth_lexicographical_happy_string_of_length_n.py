def get_happy_string(n: int, k: int) -> str:
    if k > 3 * 2 ** (n - 1):
        return ""

    options = ["a", "b", "c"]

    block_size = 2 ** (n - 1)
    index = (k - 1) // block_size
    result = options[index]

    k = (k - 1) % block_size + 1

    for i in range(1, n):
        next_options = [char for char in ["a", "b", "c"] if char != result[-1]]
        current_size = 2 ** (n - i - 1)
        index = (k - 1) // current_size
        result += next_options[index]
        k = (k - 1) % current_size + 1
    return result


print(get_happy_string(100, 300))
print(get_happy_string(10, 3))
print(get_happy_string(10, 4))

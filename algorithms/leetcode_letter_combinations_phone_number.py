def letter_combinations(digits):
    if len(digits) == 0:
        return []

    character_dict = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    result, solution = [], []

    def backtrack(current_index):
        if current_index == len(digits):
            result.append("".join(solution[:]))
            return
        for char in character_dict[digits[current_index]]:
            solution.append(char)
            backtrack(current_index + 1)
            solution.pop()

    backtrack(0)
    return result


print(letter_combinations("22"))
print(letter_combinations("23"))
print(letter_combinations("6789"))

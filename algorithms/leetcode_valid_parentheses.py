def is_valid(s: str) -> bool:
    if len(s) <= 1:
        return False
    closing_dictionary = {"(": ")", "[": "]", "{": "}"}
    current_openings = []
    for char in s:
        if char in closing_dictionary:
            current_openings.append(char)
        else:
            if len(current_openings) == 0:
                return False
            if not char == closing_dictionary[current_openings[-1]]:
                return False
            current_openings.pop()
    if len(current_openings) >= 1:
        return False
    return True


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([])"))
print(is_valid("["))
print(is_valid("([]{})"))
print(is_valid("(("))
print(is_valid("){"))
print(is_valid("{[()]}"))

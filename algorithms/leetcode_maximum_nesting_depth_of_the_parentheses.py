def max_depth(s: str) -> int:
    result = 0
    current = 0
    for char in s:
        if char == "(":
            current += 1
            if current > result:
                result = current
        elif char == ")":
            current -= 1
    return result


print(max_depth("(1+(2*3)+((8)/4))+1"))
print(max_depth("(1)+((2))+(((3)))"))
print(max_depth("()(())((()()))"))

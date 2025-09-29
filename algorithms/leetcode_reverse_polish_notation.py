import math


def eval_RPN(tokens: list[str]) -> int:
    nums = []
    for token in tokens:
        if token in "+-*/":
            b, a = nums.pop(), nums.pop()
            if token == "+":
                nums.append(a + b)
            elif token == "-":
                nums.append(a - b)
            elif token == "*":
                nums.append(a * b)
            else:
                division = a / b
                if division < 0:
                    nums.append(math.ceil(division))
                else:
                    nums.append(int(a / b))
        else:
            nums.append(int(token))
    return nums[0]


print(eval_RPN(["2", "1", "+", "3", "*"]))
print(eval_RPN(["4", "13", "5", "/", "+"]))
print(eval_RPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(eval_RPN(["10", "6", "9", "3", "+", "-11", "", "/", "", "17", "+", "5", "+"]))

def score_of_parentheses(s: str) -> int:
    score = depth = 0
    for i in range(len(s)):
        if s[i] == "(":
            depth += 1
        else:
            depth -= 1
            if s[i - 1] == "(":
                score += 1 << depth
    return score


print(score_of_parentheses("()"))
print(score_of_parentheses("(())"))
print(score_of_parentheses("()()"))

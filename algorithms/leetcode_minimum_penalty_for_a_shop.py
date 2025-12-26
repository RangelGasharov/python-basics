def best_closing_time(customers: str) -> int:
    score = 0
    max_score = 0
    close = -1

    for i in range(len(customers)):
        if customers[i] == "Y":
            score += 1
        else:
            score -= 1

        if score > max_score:
            max_score = score
            close = i

    return close + 1


print(best_closing_time("YYNY"))
print(best_closing_time(
    "YNNYYNNYYNYNNNNNYNYNYNNYNNYYYNNNNYYYNYNYNYYYNYNYYYYYYNNYNNNYYNYYYNNYYYYYNNYYNYNYNYNNNYYNNYYYYNYYYYNNNYNYNYNYYN"
    "NYYNNNYNNYYYNNYNNYYYNNNNYYYYNYNYNYYNNNNYNNNYNYNYYYNNNNNNNYNYYYYYNYYNNYNYNYNNNYYNYNNNYYNYNY"))

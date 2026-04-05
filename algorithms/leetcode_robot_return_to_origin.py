def judge_circle(moves: str) -> bool:
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


print(judge_circle("UDLR"))
print(judge_circle("UDLRU"))
print(judge_circle(""))
print(judge_circle("DDUDLRUU"))

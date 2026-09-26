import re
from typing import List


def evaluate(s: str, knowledge: List[List[str]]) -> str:
    dictionary = dict(knowledge)
    return re.sub(r"\((\w+)\)", lambda m: dictionary.get(m[1], "?"), s)


print(evaluate("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]))
print(evaluate("hi(name)", [["a", "b"]]))
print(evaluate("(a)(a)(a)aaa", [["a", "yes"]]))

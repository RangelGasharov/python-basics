def rotate_string(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    for i in range(len(s)):
        if s[i:] + s[0:i] == goal:
            return True
    return False


print(rotate_string("abcde", "cdeab"))
print(rotate_string("bbbacddceeb", "ceebbbbacdd"))
print(rotate_string("abcde", "abced"))
print(rotate_string("abcd", ""))

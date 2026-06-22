def max_number_of_balloons(text: str) -> int:
    counts = [0] * 26
    for char in text:
        counts[ord(char) - ord("a")] += 1

    def get_count(c):
        return counts[ord(c) - ord("a")]

    return min(get_count("b"), get_count("a"), get_count("l") // 2, get_count("o") // 2, get_count("n"))


print(max_number_of_balloons("balloon"))
print(max_number_of_balloons("nlaebolko"))
print(max_number_of_balloons("loonbalxballpoon"))
print(max_number_of_balloons("leetcode"))

def maximal_rectangle(matrix: list[list[str]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    result = 0

    def largest_rectangle(heights):
        stack = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area

    current_height = [0] * m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "1":
                current_height[j] += 1
            else:
                current_height[j] = 0
        largest_area = largest_rectangle(current_height)
        if largest_area > result:
            result = largest_area
    return result


print(maximal_rectangle(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]))

print(maximal_rectangle([["0"]]))
print(maximal_rectangle([["1"]]))

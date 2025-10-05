def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()
    result = []

    def dfs(row, col, visit, prev_height):
        if (row, col) in visit or row < 0 or col < 0 or row == rows or col == cols or heights[row][col] < prev_height:
            return
        visit.add((row, col))
        dfs(row + 1, col, visit, heights[row][col])
        dfs(row - 1, col, visit, heights[row][col])
        dfs(row, col + 1, visit, heights[row][col])
        dfs(row, col - 1, visit, heights[row][col])

    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])
        dfs(rows - 1, c, atlantic, heights[rows - 1][c])

    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, cols - 1, atlantic, heights[r][cols - 1])

    for r in range(rows):
        for c in range(cols):
            if (r, c) in pacific and (r, c) in atlantic:
                result.append([r, c])
    return result


print(pacific_atlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
print(pacific_atlantic([[1]]))

def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = len(board)
    cols = len(board[0])
    if cols != 9 or rows != 9:
        return False

    def is_valid_number(number):
        if not number.isdigit():
            return False
        if int(number) < 1 or int(number) > 9:
            return False
        return True

    def check_rows() -> bool:
        for i in range(rows):
            filtered_numbers = list(filter(lambda x: is_valid_number(x), board[i]))
            if len(set(filtered_numbers)) != len(filtered_numbers):
                return False
        return True

    def check_cols() -> bool:
        for i in range(cols):
            numbers = []
            for j in range(rows):
                numbers.append(board[j][i])

            filtered_numbers = list(filter(lambda x: is_valid_number(x), numbers))
            if len(set(filtered_numbers)) != len(filtered_numbers):
                return False
        return True

    def check_cells() -> bool:
        for k in range(0, 7, 3):
            for m in range(0, 7, 3):
                numbers = []
                for i in range(0 + k, 3 + k):
                    for j in range(0 + m, 3 + m):
                        numbers.append(board[j][i])
                filtered_numbers = list(filter(lambda x: is_valid_number(x), numbers))
                if len(set(filtered_numbers)) != len(filtered_numbers):
                    return False
        return True

    if not check_rows():
        return False

    if not check_cols():
        return False

    if not check_cells():
        return False

    return True


print(is_valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                       ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                       [".", "9", "8", ".", ".", ".", ".", "6", "."],
                       ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                       ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                       [".", "6", ".", ".", ".", ".", "2", "8", "."],
                       [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(is_valid_sudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                       ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                       [".", "9", "8", ".", ".", ".", ".", "6", "."],
                       ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                       ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                       [".", "6", ".", ".", ".", ".", "2", "8", "."],
                       [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(is_valid_sudoku([["7", ".", ".", ".", "4", ".", ".", ".", "."],
                       [".", ".", ".", "8", "6", "5", ".", ".", "."],
                       [".", "1", ".", "2", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", "9", ".", ".", "."],
                       [".", ".", ".", ".", "5", ".", "5", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "2", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."]]))

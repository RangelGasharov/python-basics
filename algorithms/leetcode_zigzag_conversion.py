def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s

    rows = [""] * num_rows
    curr_row = 0
    step = 1

    for char in s:
        rows[curr_row] += char
        if curr_row == 0:
            step = 1
        elif curr_row == num_rows - 1:
            step = -1
        curr_row += step

    return "".join(rows)


print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
print(convert("A", 3))

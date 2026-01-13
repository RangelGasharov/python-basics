def separate_squares(squares: list[list[int]]) -> float:
    max_y = squares[0][1] + squares[0][2]
    min_y = squares[0][1]
    total_area = 0

    for x, y, l in squares:
        if y + l > max_y:
            max_y = y + l
        if y < min_y:
            min_y = y
        total_area += l * l

    def get_area_below(line_y: float):
        area = 0
        for x, y, l in squares:
            if line_y <= y:
                continue
            elif line_y >= y + l:
                area += l * l
            else:
                area += l * (line_y - y)
        return area

    low, high = min_y, max_y

    for _ in range(80):
        mid = (low + high) / 2
        if get_area_below(mid) < total_area / 2:
            low = mid
        else:
            high = mid

    return round(low, 5)


print(separate_squares([[0, 0, 1], [2, 2, 1]]))
print(separate_squares([[17, 30, 3], [20, 26, 1], [7, 26, 5], [22, 29, 3], [6, 19, 2]]))
print(separate_squares([[522261215, 954313664, 225462], [628661372, 718610752, 10667], [619734768, 941310679, 44788],
                        [352367502, 656774918, 289036], [860247066, 905800565, 100123], [817623994, 962847576, 71460],
                        [691552058, 782740602, 36271], [911356, 152015365, 513881], [462847044, 859151855, 233567],
                        [672324240, 954509294, 685569]]))

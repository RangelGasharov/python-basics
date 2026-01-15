def maximize_square_hole_area(n: int, m: int, h_bars: list[int], v_bars: list[int]) -> int:
    def find_longest_consecutive_elements(num_set):
        max_length = 0
        for num in num_set:
            if num - 1 not in num_set:
                end = num + 1
                while end in num_set:
                    end += 1
                length = end - num
                if length > max_length:
                    max_length = length
        return max_length

    if len(h_bars) == 0 or len(v_bars) == 0:
        return 1
    h_set, v_set = set(h_bars), set(v_bars)
    max_h_bars, max_v_bars = find_longest_consecutive_elements(h_set), find_longest_consecutive_elements(v_set)
    return (min(max_h_bars, max_v_bars) + 1) ** 2


print(maximize_square_hole_area(2, 1, [2, 3], [2]))
print(maximize_square_hole_area(1, 1, [2], [2]))
print(maximize_square_hole_area(2, 3, [2, 3], [2, 4]))

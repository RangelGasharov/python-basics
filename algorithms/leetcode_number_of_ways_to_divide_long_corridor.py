def number_of_ways(corridor: str) -> int:
    mod = 10 ** 9 + 7
    n = len(corridor)

    seats = [i for i, c in enumerate(corridor) if c == 'S']

    if len(seats) == 0 or len(seats) % 2 != 0:
        return 0

    if len(seats) == 2:
        return 1

    ways = 1
    for i in range(1, len(seats) // 2):
        prev_end = seats[2 * i - 1]
        next_start = seats[2 * i]
        gap = next_start - prev_end
        ways = (ways * gap) % mod

    return ways


print(number_of_ways("S"))
print(number_of_ways("SSPSS"))
print(number_of_ways("SSPPPPPPPSSPSSPPPSSSSP"))
print(number_of_ways("SSSPSS"))
print(number_of_ways("SSPPSSPPPSSPPSSPPPSSSSPPSSPPPSSPPSSPPPSSPPPPSSSSSSSSPPSSPPPSSPPSSPPPSSSSPPSSPPPSSPPSSPPPSSPPPPSSSSSS"))
print(number_of_ways("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS"))

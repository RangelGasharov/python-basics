def furthest_distance_from_origin(moves: str) -> int:
    return len(moves) - 2 * min(moves.count("L"), moves.count("R"))


print(furthest_distance_from_origin("L_RL__R"))
print(furthest_distance_from_origin("_R__LL_"))
print(furthest_distance_from_origin("_______"))

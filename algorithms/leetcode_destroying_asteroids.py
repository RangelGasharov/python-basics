from typing import List


def asteroids_destroyed(mass: int, asteroids: List[int]) -> bool:
    asteroids.sort()
    for asteroid in asteroids:
        if mass < asteroid:
            return False
        mass += asteroid
    return True


print(asteroids_destroyed(10, [3, 9, 19, 5, 21]))
print(asteroids_destroyed(5, [4, 9, 23, 4]))
print(asteroids_destroyed(6, [4, 9, 23, 4]))

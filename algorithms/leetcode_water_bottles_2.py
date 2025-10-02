def num_water_bottles(num_bottles: int, num_exchange: int) -> int:
    sum_bottles = 0
    drinkable_bottles = num_bottles
    while drinkable_bottles >= 1:
        sum_bottles += drinkable_bottles
        drinkable_bottles = 1 * (num_bottles >= num_exchange)
        num_bottles -= 1 * num_exchange
        num_bottles += drinkable_bottles
        num_exchange += 1
    return sum_bottles


print(num_water_bottles(13, 6))
print(num_water_bottles(10, 3))
print(num_water_bottles(20, 4))

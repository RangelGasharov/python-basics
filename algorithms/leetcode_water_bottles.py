def num_water_bottles(num_bottles: int, num_exchange: int) -> int:
    sum_bottles = 0
    drinkable_bottles = num_bottles
    while drinkable_bottles >= 1:
        sum_bottles += drinkable_bottles
        drinkable_bottles = num_bottles // num_exchange
        num_bottles -= drinkable_bottles * num_exchange
        num_bottles += drinkable_bottles
    return sum_bottles


print(num_water_bottles(9, 3))
print(num_water_bottles(15, 4))
print(num_water_bottles(20, 4))

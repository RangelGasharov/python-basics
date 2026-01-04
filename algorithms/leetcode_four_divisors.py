import math


def sum_four_divisors(nums: list[int]) -> int:
    sum_of_divisors = 0

    for num in nums:
        current_sum = 1 + num
        amount_of_divisors = 2
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                current_sum += i
                if num / i != i:
                    current_sum += int(num / i)
                    amount_of_divisors += 1
                amount_of_divisors += 1
                if amount_of_divisors > 4:
                    break
        if amount_of_divisors == 4:
            sum_of_divisors += current_sum
    return sum_of_divisors


print(sum_four_divisors([21, 4, 7]))
print(sum_four_divisors([21, 21]))
print(sum_four_divisors([1, 2, 3, 4, 5]))

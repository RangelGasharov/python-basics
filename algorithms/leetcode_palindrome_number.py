def is_palindrome(number):
    number_string = str(number)
    left = 0
    right = len(number_string) - 1
    while left < right:
        if number_string[left] != number_string[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome(-121))
print(is_palindrome(121))
print(is_palindrome(10))
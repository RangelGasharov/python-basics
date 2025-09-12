def does_first_player_win_string_game(text):
    vowels = "aeiou"
    for letter in text:
        if letter in vowels:
            return True
    return False


print(does_first_player_win_string_game("leetcoder"))
print(does_first_player_win_string_game("parentheses"))
print(does_first_player_win_string_game("application"))
print(does_first_player_win_string_game("bbcd"))

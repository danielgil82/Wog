import regex

def validate_input(msg: str, lower_range: int, higher_range: int):
    user_choice = input(msg)

    # if not numeric or not in range.
    while not regex.fullmatch(r"[0-9]", user_choice) or int(user_choice) > higher_range or int(user_choice) < lower_range:
        print(f"Please choose a number between {lower_range} and {higher_range}")
        user_choice = input()

    return user_choice
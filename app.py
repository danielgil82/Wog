import regex

def welcome(name: str):
    print(f"Hello {name} and welcome to the World Of Games: The Epic Journey")

def start_play():
    games_msg = (f"Please choose a game to play:\n"
           f"1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
           f"2. Guess Game - guess a number and see if you chose like the computer.\n"
           f"3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")

    validate_input(games_msg, 1, 3)

    difficulty_msg = f"Please choose difficulty level between 1 to 5\n"

    validate_input(difficulty_msg, 1, 5)


def validate_input(msg: str, lower_range: int, higher_range: int):
    user_choice = input(msg)

    # if not numeric or not in range.
    while not regex.fullmatch(r"[0-9]", user_choice) or int(user_choice) > higher_range or int(user_choice) < lower_range:
        print(f"Please choose between {lower_range} and {higher_range}")
        user_choice = input(msg)
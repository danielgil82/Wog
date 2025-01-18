from Score.utils import validate_input
import random
import time

random.seed(time.time())
LOWER_RANGE = 0

def play(difficulty: str):
    generated_number = generate_number(difficulty)
    user_input = get_guess_from_user(difficulty)
    return compare_results(generated_number, user_input)


def generate_number(difficulty: str):
    return random.randint(LOWER_RANGE, int(difficulty))

def get_guess_from_user(difficulty: str):
    return int(validate_input(f"Please choose a number between 0 and {difficulty}\n",
                          lower_range=LOWER_RANGE,
                          higher_range=int(difficulty)))

def compare_results(generated_number: int, user_input: int):
    return generated_number == user_input
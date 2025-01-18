from currency_converter import CurrencyConverter
import random
import time

random.seed(time.time())
c = CurrencyConverter()
LOWER_RANGE = 1
HIGHER_RANGE = 100


def play(difficulty: str):
    generated_amount_in_usd, generated_amount_in_ils, interval = get_money_interval(int(difficulty))
    user_guess = get_guess_from_user(generated_amount_in_usd)

    return compare_results(interval, user_guess, generated_amount_in_ils)

def get_money_interval(difficulty: int):
    generated_amount_in_usd = random.randint(LOWER_RANGE, HIGHER_RANGE)
    generated_amount_in_ils = c.convert(generated_amount_in_usd, 'USD', 'ILS')
    interval = 10 - difficulty

    return generated_amount_in_usd, generated_amount_in_ils, interval

def get_guess_from_user(generated_amount: int):
    msg = f"Guess how much {generated_amount} USD is in ILS\n"
    return int(input(msg))


def compare_results(interval: int, user_guess: int, generated_amount_in_ils):
    return abs(user_guess - generated_amount_in_ils) <= interval
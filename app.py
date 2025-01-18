from utils import validate_input
import guess_game
import currency_roulette_game
import memory_game

def welcome(name: str):
    print(f"Hello {name} and welcome to the World Of Games: The Epic Journey")
    start_play()

def start_play():
    games_msg = (f"Please choose a game to play:\n"
           f"1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
           f"2. Guess Game - guess a number and see if you chose like the computer.\n"
           f"3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")

    game_number = validate_input(games_msg, 1, 3)

    difficulty_msg = f"Please choose difficulty level between 1 to 5\n"

    difficulty_level = validate_input(difficulty_msg, 1, 5)

    if game_number == '1':
        print(memory_game.play(difficulty_level))
    elif game_number == '2':
        print(guess_game.play(difficulty_level))
    else:
        print(currency_roulette_game.play(difficulty_level))

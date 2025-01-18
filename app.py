from Score.utils import validate_input
from Score.score import add_score
import guess_game
import currency_roulette_game
import memory_game

def welcome(name: str):
    print(f"Hello {name} and welcome to the World Of Games: The Epic Journey")
    start_play()

def start_play():
    wanna_play = 'yes'

    while wanna_play == 'yes':
        games_msg = (f"Please choose a game to play:\n"
               f"1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
               f"2. Guess Game - guess a number and see if you chose like the computer.\n"
               f"3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")

        game_number = validate_input(games_msg, 1, 3)

        difficulty_msg = f"Please choose difficulty level between 1 to 5\n"

        difficulty_level = validate_input(difficulty_msg, 1, 5)

        result = False
        if game_number == '1':
            result = memory_game.play(difficulty_level)
        elif game_number == '2':
            result = guess_game.play(difficulty_level)
        else:
            result = currency_roulette_game.play(difficulty_level)

        if result:
            print(f"inside add_score")
            add_score(difficulty_level)

        wanna_play = input(f"Do you still wanna play?\n Please enter yes or no")

    print(f"Thank you for playing")

if __name__ == "__main__":
    welcome(input("Please enter your name\n"))
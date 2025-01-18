from app import welcome, start_play
from guess_game import *

welcome(input("Please enter your name\n"))
game_number, difficulty = start_play()

play(difficulty)


from app import welcome, start_play

welcome(input("Please enter your name\n"))
game_number, difficulty_level = start_play()
print(f"User choose game number {game_number}, "
      f"with difficulty level {difficulty_level}")

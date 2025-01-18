import random
import time
import os
random.seed(time.time())

LOWER_RANGE = 1
HIGHER_RANGE = 101
TIME_SLEEP = 0.7

def play(difficulty: str):
    generated_sequence = generate_sequence(int(difficulty))
    time.sleep(TIME_SLEEP)
    os.system('cls' if os.name == 'nt' else 'clear')
    user_sequence = get_list_from_user(int(difficulty))

    return is_list_equal(generated_sequence, user_sequence)

def generate_sequence(sequence_len: int):
    sequence = []
    for x in range(sequence_len):
        generated_number = random.randint(LOWER_RANGE, HIGHER_RANGE)
        sequence.append(generated_number)

    return sequence

def get_list_from_user(sequence_len: int):
    print(f"Please enter {sequence_len} numbers: ")
    sequence = []
    for x in range(sequence_len):
        print(f"{x + 1} number: ")
        sequence.append(int(input()))

    return sequence

def is_list_equal(expected_sequence: [], actual_sequence: []):
    for x in range(len(expected_sequence)):
        if expected_sequence[x] != actual_sequence[x]:
            return False

    return True
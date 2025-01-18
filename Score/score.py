from Score.utils import SCORES_FILE_NAME, BAD_RETURN_CODE

def add_score(difficulty: str):
    try:
        score = read_score()
        if score:
            score = int(score[0]) + int(difficulty) * 3 + 5
        else:
            score =  int(difficulty) * 3 + 5
        
        file = open(SCORES_FILE_NAME, "w+")
        file.write(str(score))
        file.close()
        
    except Exception:
        print(f"Error {BAD_RETURN_CODE} something went wrong"
              f"'{SCORES_FILE_NAME}' does not exist. It will be created.")


def read_score():
    file = ""
    try:
        file = open(SCORES_FILE_NAME, "r+")
        score = file.readlines()

        return score
    except FileNotFoundError:
        print(f"Error {BAD_RETURN_CODE} something went wrong"
              f"'{SCORES_FILE_NAME}' does not exist. It will be created.")

    finally:
        file.close()
from flask import Flask, render_template
from Score import score, utils

app = Flask(__name__)

@app.route('/score')
def score_server():
   game_score = score.read_score()
   if game_score == '':
      return render_template('error.html', ERROR=utils.BAD_RETURN_CODE)
   else:
      return render_template('index.html', SCORE=game_score[0])

if __name__ == '__main__':
   app.run()
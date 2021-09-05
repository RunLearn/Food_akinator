from flask import Flask, render_template, request
import random
from data import questions
from function import calculate_probabilites

app = Flask(__name__)


questions_so_far = []
answers_so_far = []

@app.route('/')
def index():
    global questions_so_far, answers_so_far

    question = request.args.get('question')
    answer = request.args.get('answer')
    if question and answer:
        questions_so_far.append(int(question))
        answers_so_far.append(float(answer))

    probabilities = calculate_probabilites(questions_so_far, answers_so_far)
    print("probabilities", probabilities)

    questions_left = list(set(questions.keys()) - set(questions_so_far))

    result = sorted(probabilities, key=lambda p: p['probability'], reverse=True)[0]

    if len(questions_left) == 0 or (result['probability'] > 0.9):

        return render_template('index.html', result=result['name'], probability=result['probability'])
    else:
        next_question = random.choice(questions_left)
        return render_template('index.html', question=next_question, question_text=questions[next_question],probability=probabilities)


if __name__ == '__main__':
    app.run()



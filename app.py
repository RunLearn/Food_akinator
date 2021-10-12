from flask import Flask, render_template, request
import random
from data import questions
from function import calculate_probabilites, question_choice, food_img, best_proba

app = Flask(__name__)


questions_so_far = []
answers_so_far = []


@app.route('/', methods=['GET','POST'])
def index():
    global questions_so_far, answers_so_far

    # if request.method == 'POST':
    #     value = request.form['reset']
    #     value = str(value)
    #     print(value)
    #
    # if value:
    #     print('게임을 다시 시작합니다.')




    question = request.args.get('question')
    answer = request.args.get('answer')
    if question and answer:
        questions_so_far.append(int(question))
        answers_so_far.append(float(answer))

    probabilities = calculate_probabilites(questions_so_far, answers_so_far)
    print("probabilities", probabilities)

    questions_left = list(set(questions.keys()) - set(questions_so_far))

    result = sorted(probabilities, key=lambda p: p['probability'], reverse=True)[0]

    # if len(questions_left) == 0 or (result['probability'] > 0.7):
    if len(questions_left) == 0 or best_proba(probabilities) == True:
        return render_template('index.html', result=result['name'], probability=result['probability'],result_img = food_img(result['name']))
    else:
        if len(questions_left) % 2 == 1:
            next_question = random.choice(questions_left)
        else:
            next_question = question_choice(questions_left)

    return render_template('index.html', question=next_question, question_text=questions[next_question],probability=probabilities)


if __name__ == '__main__':
    app.run()
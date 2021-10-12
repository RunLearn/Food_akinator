from data import foods
import numpy as np


def calculate_probabilites(questions_so_far, answers_so_far):
    probabilities = []
    for food in foods:
        probabilities.append({
            'name': food['name'],
            'probability': calculate_food_probability(food, questions_so_far, answers_so_far)
        })

    return probabilities

def calculate_food_probability(food, questions_so_far, answers_so_far):
    # Prior
    P_food = 1 / len(foods)

    # Likelihood
    #해당 음식이 맞을 확률
    P_answers_given_food = 1
    #해당 음식이 아닐 확률
    P_answers_given_not_food = 1

    for question, answer in zip(questions_so_far, answers_so_far):
        #해당 음식의 맞을 확률 *= 둘중 큰 값( 1 - 절대값(입력된 정답값 - DB의 정답값 ) , 0.01 )
        P_answers_given_food *= max(1 - abs(answer - food_answer(food, question)), 0.01)

        #해당 음식의 아닐 확률 = 평균( 입력된 푸드외에 모든 경우에 대해서 (절대값(입력된 정답값 - DB의 정답값 )))
        P_answer_not_food = np.mean([1 - abs(answer - food_answer(not_food, question))
                                      for not_food in foods
                                      if not_food['name'] != food['name']])

        #해당 음식이 아닐 확률 *= 둘중 큰값( 해당 음식이 아닐 확률, 0.01)
        P_answers_given_not_food *= max(P_answer_not_food, 0.01)

    # 공식
    #사전 확률(긍정) * 음식이 맞을 확률 + 사전 확률(부정) * 음식이 아닐 확률
    P_answers = P_food * P_answers_given_food + \
                (1 - P_food) * P_answers_given_not_food

    # Bayes Theorem
    P_character_given_answers = (
        P_answers_given_food * P_food) / P_answers

    return np.round(P_character_given_answers,5)

def food_answer(food, question):
    if question in food['answers']:
        return food['answers'][question]
    return 0.5

def question_choice(question,answer):
    return 0

def food_img(result):
    return (f'img/{result}.png')

from data import foods, food_df
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

#엔트로피를 이용하여 최적의 질문 선별

# 엔트로피
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts = True)
    entropy = -np.sum([(counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
    return entropy

# 정보이득
def InfoGain(data, split_attribute_name, target_name):
    # 전체 엔트로피 계산
    total_entropy = entropy(data[target_name])
    # print('Entropy(D) = ', round(total_entropy, 5))

    # 가중 엔트로피 계산
    vals, counts = np.unique(data[split_attribute_name], return_counts=True)
    Weighted_Entropy = np.sum([(counts[i] / np.sum(counts)) *
                               entropy(data.where(data[split_attribute_name] == vals[i]).dropna()[target_name])
                               for i in range(len(vals))])
    # print('H(', split_attribute_name, ') = ', round(Weighted_Entropy, 5))

    # 정보이득 계산
    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain

def question_choice(questions):
    best_Info = 0
    for i in questions:
        check = InfoGain(food_df,i,'name')
        if check > best_Info:
            best_Info = check
            best_question = i
    else:
        print(best_question,best_Info)
        toggle_random = 1
        return best_question

def food_img(result):
    return (f'img/{result}.png')

def best_proba(probabilities):
    probabilities_list=[]
    for i in probabilities:
        probabilities_list.append(i['probability'])

    max_proba=max(probabilities_list)
    avg_proba=sum(probabilities_list)/len(probabilities_list)
    if max_proba >= avg_proba+0.5:
        return True
    else:
        return False
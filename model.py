import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydot as pydot
from Tools.scripts.dutree import display
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import graphviz
from sklearn.utils import graph

from data import foods,questions

new_foods = []
food_name = []

for i in foods:
  food_name.append(i['name'])
  new_foods.append(i['answers'])

food_df = pd.DataFrame(new_foods)
food_df['name'] = food_name

y = food_df.iloc[:,-1:]
X = food_df.iloc[:,:-1]

A = 0
for i in range(1,30):
  for j in range(1,30):
    model = DecisionTreeClassifier(max_depth=i,min_samples_leaf=j, random_state=42).fit(X,y)
    check = model.score(X,y)

    if check > A:
      A = check
      best_parameter = (i,j)
      print(f'max_depth : {i}, min_samples_leaf : {j} model_score : {model.score(X,y)}')


model = DecisionTreeClassifier(max_depth=best_parameter[0],min_samples_leaf=best_parameter[1], random_state=42).fit(X,y)
print(f'BEST_Parameter = max_depth : {best_parameter[0]}, min_samples_leaf : {best_parameter[1]} model_score : {model.score(X,y)}')

# 트리 구조 시각화하기
# 결정트리 시각화


# dot_graph = export_graphviz(model, out_file='dot.png',
#                 class_names=list(y['name']),
#                 feature_names=list(questions.values()),
#                 filled=True)

export_graphviz(model, out_file='tree.dot',
                class_names=list(y['name']),
                feature_names=list(questions.values()),
                filled=True,
                impurity=False)

(graph,) = pydot.graph_from_dot_file('C:/Users/seojaeyong/Documents/GitHub/Food_akinator/tree.dot',encoding='utf8')

graph.write_png('tree.png')


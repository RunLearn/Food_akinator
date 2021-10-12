import pandas as pd

questions = {
    1: '치즈가 들어간 음식 어때?',
    2: '포장마차에 파는 음식어때?',
    3: '샤브샤브 어때?',
    4: '무한리필집 가는거 어때?',
    5: '야식먹을래?',
    6: '닭요리 어때?',
    7: '계란 좋아해?',
    8: '양식 어때?',
    9: '고기가 들어가는 음식어때?',
    10: '튀긴음식 어때?',
    11: '디저트 먹을래?',
    12: '면요리 어때?',
    13: '국물있는 음식 어때?',
    14: '회는 어때?',
    15: '밥먹고 싶어?',
    16: '매콤하거나 자극적인 음식은 어때?',
    17: '해물류가 들어가도 괜찮아?',
    18: '술안주 먹을래?',     # 술과함께먹는음식어때
    19: '달달한 거 어때?'

}



foods = [
# 한식 중식
    {'name': '김밥', 'answers': {1:0.1, 2:0, 3:0, 4:0.2, 5:0, 6:0, 7:0.7, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:1, 16:0, 17:0, 18:0, 19:0}},
    {'name': '떡볶이', 'answers': {1:0.7, 2:1, 3:0, 4:0, 5:0.5, 6:0, 7:0.2, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0.3, 14:0, 15:0, 16:1, 17:0, 18:0, 19:0}},
    {'name': '삼겹살 or 목살', 'answers': {1:0, 2:0, 3:0, 4:1, 5:0.3, 6:0, 7:0, 8:0, 9:1, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0.3, 16:0.3, 17:0, 18:1, 19:0}},
    {'name': '국밥 or 찌개', 'answers': {1:0, 2:0.7, 3:0, 4:0, 5:0.2, 6:0, 7:0.2, 8:0, 9:0.5, 10:0, 11:0, 12:0, 13:1, 14:0, 15:1, 16:0.3, 17:0, 18:1, 19:0}},
    {'name': '칼국수 or 팥죽', 'answers': {1:0, 2:0.5, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:1, 13:1, 14:0, 15:0, 16:0.2, 17:0.2, 18:0, 19:0.5}},
    {'name': '생선구이', 'answers': {1:0, 2:0.2, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:1, 16:0, 17:0, 18:0.4, 19:0}},
    {'name': '짜장면', 'answers':{1:0, 2:0.3, 3:0, 4:0, 5:0, 6:0, 7:0.1, 8:0, 9:0.3, 10:0, 11:0, 12:1, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0.3}},
    {'name': '짬뽕', 'answers': {1:0, 2:1, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0.3, 10:0, 11:0, 12:1, 13:1, 14:0, 15:0.5, 16:1, 17:1, 18:0.5, 19:0}},
    {'name': '해물덮밥', 'answers':{1:0, 2:0.3, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0.3, 10:0, 11:0, 12:0, 13:0, 14:0, 15:1, 16:0.2, 17:1, 18:0, 19:0.3}},
    {'name': '볶음밥', 'answers': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1, 8:0, 9:0.2, 10:0, 11:0, 12:0, 13:0, 14:0, 15:1, 16:0, 17:0.2, 18:0, 19:0.5}},
    {'name': '냉면', 'answers':{1:0, 2:0, 3:0, 4:0, 5:0.3, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:1, 13:1, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0}},        # 주류
    {'name': '매운탕', 'answers': {1:0, 2:1, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:1, 14:1, 15:0.5, 16:1, 17:1, 18:1, 19:0}},
    {'name': '샐러드 or 과일', 'answers': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1, 8:0.3, 9:0, 10:0, 11:1, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:1}},

    {'name' : '파스타','answers': {1:1, 2:0.1, 3:0, 4:0, 5:0, 6:0, 7:1, 8:1, 9:0.5, 10:0, 11:0, 12:1, 13:0, 14:0, 15:0, 16:0.5, 17:0.5, 18:0, 19:0.3}},
    {'name' : '스테이크','answers': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:1, 9:1, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0.2, 17:0, 18:0, 19:0}},
    {'name' : '피자','answers': {1:1, 2:0, 3:0, 4:0.5, 5:1, 6:0, 7:0, 8:1, 9:0.5, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0.5, 17:0, 18:0.3, 19:0.7}},
    {'name' : '치킨','answers':{1:0.3, 2:0.3, 3:0, 4:0.3, 5:1, 6:1, 7:0, 8:0, 9:0, 10:1, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0.5, 17:0, 18:1, 19:0.5}},

    {'name' : '초밥','answers': {1:0, 2:0.3, 3:0, 4:1, 5:0.5, 6:0, 7:0.3, 8:0, 9:0.1, 10:0, 11:0, 12:0, 13:0, 14:0.3, 15:1, 16:0, 17:0.3, 18:0, 19:0.3}},
    {'name' : '회','answers': {1:0, 2:0.3, 3:0, 4:0, 5:0.5, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:1, 15:0, 16:0, 17:0, 18:1, 19:0}},
    {'name' : '돈까스','answers': {1:0.5, 2:0, 3:0, 4:0.2, 5:0.3, 6:0, 7:0, 8:0, 9:1, 10:1, 11:0, 12:0, 13:0, 14:0, 15:0.3, 16:0.3, 17:0, 18:0, 19:0.3}},
    {'name' : '샤브샤브','answers': {1:0, 2:0, 3:1, 4:1, 5:0, 6:0, 7:0, 8:0, 9:1, 10:0, 11:0, 12:0, 13:1, 14:0, 15:0, 16:0.5, 17:0, 18:0.2, 19:0}},

    {'name' : '햄버거','answers': {1:1, 2:0.2, 3:0, 4:0, 5:1, 6:0, 7:0.5, 8:1, 9:1, 10:0, 11:1, 12:0, 13:0, 14:0, 15:0, 16:0.5, 17:0, 18:0, 19:1}},        # 에이드, 샐러드, 과일주스
    {'name' : '라면','answers': {1:1, 2:1, 3:0, 4:0.2, 5:1, 6:0, 7:1, 8:0, 9:0, 10:0, 11:0.1, 12:1, 13:1, 14:0, 15:0.1, 16:1, 17:0, 18:0.5, 19:0}},
    {'name' : '닭갈비','answers': {1:1, 2:0.2, 3:0, 4:0, 5:0.5, 6:1, 7:0, 8:0.3, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:1, 17:0, 18:0.5, 19:0.5}},
    {'name' : '토스트','answers': {1:0.5, 2:0, 3:0, 4:0, 5:0.5, 6:0, 7:1, 8:1, 9:0, 10:0, 11:1, 12:0, 13:0, 14:0, 15:0, 16:0.3, 17:0, 18:0, 19:1}}
]

new_foods = []
food_name = []

for i in foods:
  food_name.append(i['name'])
  new_foods.append(i['answers'])

food_df = pd.DataFrame(new_foods)
food_df['name'] = food_name

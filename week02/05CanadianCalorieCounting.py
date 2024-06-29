# 햄버거, 사이드, 음료, 디저트 선택에 따라 총 칼로리를 계산하기

def calorie_count():
    # 메뉴 칼로리 정보
    burgers = [461, 431, 420, 0]
    sides = [100, 57, 70, 0]
    drinks = [130, 160, 118, 0]
    desserts = [167, 266, 75, 0]

    # 사용자의 선택 입력 받기
    burger_choice = int(input()) - 1
    side_choice = int(input()) - 1
    drink_choice = int(input()) - 1
    dessert_choice = int(input()) - 1

    # 총 칼로리 계산하기
    total_calories = burgers[burger_choice] + sides[side_choice] + drinks[drink_choice] + desserts[dessert_choice]

    # 결과 출력하기
    print(f"Your total Calorie count is {total_calories}.")

calorie_count()

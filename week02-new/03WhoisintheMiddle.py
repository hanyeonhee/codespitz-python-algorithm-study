# 세 숫자 중 중간값을 찾기

def who_is_in_the_middle():
    # 세 숫자 입력 받기
    a = int(input())
    b = int(input())
    c = int(input())

    # 중간값 찾기
    middle_value = sorted([a, b, c])[1]

    # 결과 출력하기
    print(middle_value)

who_is_in_the_middle()
# 전화번호가 텔레마케터 번호인지 확인하기
# 1번째와 4번째숫자가 8 또는 9이어야 함
# 2번째와 3번째 숫자가 동일해야 함!

def is_telemarketer():
    # 전화번호의 각 자리 숫자를 입력 받기
    first_digit = int(input())
    second_digit = int(input())
    third_digit = int(input())
    fourth_digit = int(input())

    # 조건을 확인하고 결과를 출력하기
    if (first_digit in [8, 9]) and (fourth_digit in [8, 9]) and (second_digit == third_digit):
        print("ignore")
    else:
        print("answer")

is_telemarketer()

# 입력된 날짜가 2월 18일 전인지, 후인지, 같은지 판단하기

def special_day():
    # 날짜 입력 받기
    month = int(input())
    day = int(input())

    # 날짜 비교 후 결과 출력하기
    if month < 2 or (month == 2 and day < 18):
        print("Before")
    elif month == 2 and day == 18:
        print("Special")
    else:
        print("After")

special_day()

# 문자열에서 :) 와 :( 이모티콘의 개수를 세어 행복한지 슬픈지 판단하기

def happy_or_sad():
    # 문자열 입력 받기
    input_str = input()

    # 각 이모티콘의 개수 세기
    happy_count = input_str.count(":-)")
    sad_count = input_str.count(":-(")

    # 결과 출력하기
    if happy_count > sad_count:
        print("happy")
    elif sad_count > happy_count:
        print("sad")
    elif happy_count == 0 and sad_count == 0:
        print("none")
    else:
        print("unsure")

happy_or_sad()

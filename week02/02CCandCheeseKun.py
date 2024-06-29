def cc_satisfaction():
    # 피자의 너비와 추가 치즈 비율을 입력 받기
    width = int(input())
    extra_cheesiness = int(input())

    # 만족도 조건을 확인하고 결과 출력하기
    if width == 3 and extra_cheesiness >= 95:
        print("C.C. is absolutely satisfied with her pizza.")
    elif width == 1 and extra_cheesiness <= 50:
        print("C.C. is fairly satisfied with her pizza.")
    else:
        print("C.C. is very satisfied with her pizza.")

cc_satisfaction()

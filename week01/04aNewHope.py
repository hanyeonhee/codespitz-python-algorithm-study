
N = int(input("정수 N을 입력: "))

# 'far' 단어를 N번 반복하는 문장을 생성.
# 마지막 'far' 뒤에는 쉼표가 오지 않도록 처리.
far_list = ["far"] * N
far_phrase = ", ".join(far_list)

# 최종 문장을 생성.
result = f"A long time ago in a galaxy {far_phrase} away..."

print(result)

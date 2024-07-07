# CCC '11 S1 - English or French?
# https://dmoj.ca/problem/ccc11s1

def is_english_or_french(text):
    t_count = text.count('t') + text.count('T')
    s_count = text.count('s') + text.count('S')

    if t_count > s_count:
        return "English"
    else:
        return "French"


# 입력 받기
N = int(input())
text = ""
for _ in range(N):
    text += input()

# 결과 출력
result = is_english_or_french(text)
print(result)
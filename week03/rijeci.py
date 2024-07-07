# COCI '13 Contest 3 #1 Riječi
# https://dmoj.ca/problem/coci13c3p1

def count_letters(K):
    # 초기 상태: A = 1, B = 0
    a, b = 1, 0

    for _ in range(K):
        # A는 B로 변환되고, B는 BA로 변환됨
        # 따라서 새로운 A의 개수는 이전의 B의 개수와 같고,
        # 새로운 B의 개수는 이전의 A와 B의 개수의 합과 같음
        a, b = b, a + b

    return a, b


# 입력 받기
K = int(input())

# 결과 계산 및 출력
a_count, b_count = count_letters(K)
print(a_count, b_count)
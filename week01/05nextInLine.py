young = int(input("가장 어린 자녀의 나이: "))

middle = int(input("중간 자녀의 나이: "))

# 등차수열의 성질을 이용하여 가장 큰 자녀의 나이 계산
old = middle + (middle - young)

# 가장 큰 자녀의 나이를 출력합니다.
print(old)

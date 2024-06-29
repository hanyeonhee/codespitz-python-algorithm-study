import math

radius = int(input("radius: "))

height = int(input("height: "))

# 원뿔의 부피를 계산
volume = (1/3) * math.pi * radius**2 * height

# 부피를 소수점 둘째 자리까지 출력
print(f"{volume:.2f}")

# CCC '11 S2 - Multiple Choice
# https://dmoj.ca/problem/ccc11s2

# 문제 개수 입력 받기
N = int(input())

# 학생 답안 입력 받기
student_answers = [input().strip() for _ in range(N)]

# 정답 입력 받기
correct_answers = [input().strip() for _ in range(N)]

# 정답 개수 세기
correct_count = sum(1 for student, correct in zip(student_answers, correct_answers) if student == correct)

# 결과 출력
print(correct_count)
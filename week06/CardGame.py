# 2144. Cleaning the Room
# https://acm.timus.ru/problem.aspx?space=1&num=2144

def can_arrange_boxes():
    n = int(input())  # 박스의 수 입력
    boxes = []

    # 각 박스의 액션 피규어 크기 정보 입력
    for _ in range(n):
        box = list(map(int, input().split()))
        figures = sorted(box[1:])  # 각 박스 내의 피규어를 정렬
        boxes.append(figures)

    # 박스들을 첫 번째 피규어의 크기를 기준으로 정렬
    boxes.sort(key=lambda x: x[0])

    all_figures = []
    for box in boxes:
        # 각 박스의 피규어들이 이전 피규어들보다 크거나 같은지 확인
        if all_figures and box[0] < all_figures[-1]:
            return "NO"
        all_figures.extend(box)

    # 모든 피규어가 오름차순으로 정렬되어 있는지 확인
    for i in range(1, len(all_figures)):
        if all_figures[i] < all_figures[i - 1]:
            return "NO"

    return "YES"


# 결과 출력
print(can_arrange_boxes())
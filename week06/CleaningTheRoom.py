# CCC '99 S1 Card Game
# https://dmoj.ca/problem/ccc99s1
def card_game_start():
    # 카드 수량 초기화
    card_quantities = {'two': 4, 'three': 4, 'four': 4, 'five': 4, 'six': 4,
                       'seven': 4, 'eight': 4, 'nine': 4, 'ten': 4, 'jack': 4,
                       'queen': 4, 'king': 4, 'ace': 4}

    num_cards = 52
    points_player_a = 0
    points_player_b = 0
    deck = []

    # 카드 입력 받기
    for _ in range(num_cards):
        card = input().strip().lower()
        if card not in card_quantities:
            exit("정확한 카드가 아닙니다.")

        card_count = card_quantities[card]
        if card_count == 0:
            exit("해당 카드가 더 이상 없습니다.")

        card_quantities[card] -= 1
        deck.append(card)

        # 특수 카드 처리 및 점수 계산
        points_player_a, points_player_b = process_special_cards(
            points_player_a, points_player_b, deck
        )

    # 최종 점수 출력
    print(f"Player A: {points_player_a} point(s).")
    print(f"Player B: {points_player_b} point(s).")


def process_special_cards(points_player_a, points_player_b, deck):
    """
    카드 덱에서 모든 특수 카드의 상태를 검사하고 해당 카드에 따른 점수를 업데이트합니다.

    Parameters:
    - points_player_a: 플레이어 A의 현재 점수
    - points_player_b: 플레이어 B의 현재 점수
    - deck: 현재까지의 카드 덱

    Returns:
    - 업데이트된 플레이어 A와 B의 점수
    """
    special_cards = [['jack', -2, -1, 1], ['queen', -3, -2, 2],
                     ['king', -4, -3, 3], ['ace', -5, -4, 4]]

    for special_card in special_cards:
        points_player_a, points_player_b = (
            process_special_card(deck, points_player_a, points_player_b,
                                 special_card))
    return points_player_a, points_player_b


def process_special_card(deck, points_player_a, points_player_b,
                         special_card_info):
    """
    특정 특수 카드에 대해 조건을 검사하고 점수를 업데이트합니다.

    Parameters:
    - deck: 현재까지의 카드 덱
    - points_player_a: 플레이어 A의 현재 점수
    - points_player_b: 플레이어 B의 현재 점수
    - special_card_info: 특수 카드에 대한 정보를 담고 있는 리스트
    (형식: [카드 식별자, 카드 음수 인덱스, 검사 시작 인덱스, 부여할 점수])

    Returns:
    - 업데이트된 플레이어 A와 B의 점수
    """
    card_identifier, negative_special_card_index, check_start_index, card_points = special_card_info

    if is_special_card_condition_met(deck, card_identifier,
                                     negative_special_card_index,
                                     check_start_index):
        target_index = len(deck) + negative_special_card_index
        return award_points(points_player_a, points_player_b, target_index,
                            card_points)
    return points_player_a, points_player_b


def is_special_card_condition_met(
        deck, special_card_identifier, negative_special_card_index,
        check_start_index):
    """
    카드 덱에서 특정 카드의 조건이 만족되는지 검사합니다.

    Parameters:
    - deck: 현재까지의 카드 덱
    - special_card_identifier: 특수 카드 식별자
    - negative_special_card_index: 특수 카드의 음수 인덱스
    - check_start_index: 검사할 시작 카드들의 시작 인덱스

    Returns:
    - 조건이 만족되면 True, 그렇지 않으면 False
    """
    return (len(deck) >= -negative_special_card_index
            and deck[negative_special_card_index] == special_card_identifier
            and no_high_card_in_range(deck[check_start_index:]))


def no_high_card_in_range(cards):
    """
    주어진 카드 범위 내에 높은 카드가 있는지 검사합니다.

    Parameters:
    - cards: 검사할 카드 목록

    Returns:
    - 범위 내에 높은 카드가 없으면 True, 있으면 False
    """
    high_cards = {'jack', 'queen', 'king', 'ace'}
    return not any(card in high_cards for card in cards)


def award_points(points_player_a, points_player_b, special_card_index, points):
    """
    특정 플레이어에게 점수를 부여합니다.

    Parameters:
    - points_player_a: 플레이어 A의 현재 점수
    - points_player_b: 플레이어 B의 현재 점수
    - special_card_index: 특수 카드의 인덱스; 짝수면 A, 홀수면 B에게 점수 부여
    - points: 부여할 점수

    Returns:
    - 업데이트된 플레이어 A와 B의 점수
    """
    if special_card_index % 2 == 0:
        points_player_a += points
        print(f"Player A scores {points} point(s).")
    else:
        points_player_b += points
        print(f"Player B scores {points} point(s).")
    return points_player_a, points_player_b


# 게임 시작
card_game_start()
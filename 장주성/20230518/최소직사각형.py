def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0

    for card in sizes:
        width, height = card

        # 지금까지 만난 가장 큰 가로 길이를 저장.
        max_width = max(max_width, max(width, height))
        # 가로와 세로 사이의 최솟값을 지금까지 만난 가장 큰 세로 길이로 저장
        max_height = max(max_height, min(width, height))

    answer = max_width * max_height

    return answer

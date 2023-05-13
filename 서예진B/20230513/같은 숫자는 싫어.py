from collections import deque
def solution(arr):
    answer = deque()
    # 배열의 마지막 원소를 pop 하고 기준으로 설정
    prev = arr.pop()
    answer.appendleft(prev)
    while len(arr) > 0:  # 배열이 비어있을 때까지 반복
        now = arr.pop()  
        if prev != now:  # 이전 원소와 다르면 
            answer.appendleft(now)  # 덱의 앞부분에 추가
            prev = now  # 기준 변경
    # 리스트 형식으로 반환
    return list(answer)
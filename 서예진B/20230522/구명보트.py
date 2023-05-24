from collections import deque

def solution(people, limit):
    answer = 0
    n = len(people)
    # 사람 무게순으로 정렬
    people.sort()
    q = deque(people)
    
    # 총 보트 수
    total = 0
    while q:
        # 혼자 남았을 때는 무조건 혼자 타고 상황 종료 
        if len(q) == 1:
            total += 1
            q.pop()
            break
        # 현재 가장 무거운 사람과 가장 가벼운 사람의 무게 합이 limit보다 작거나 같으면 같이 탐
        if q[-1] + q[0] <= limit:
            total += 1
            q.popleft()
            q.pop()
            
        # 가장 가벼운 사람과도 같이 타지 못하기 때문에 가장 무거운 사람은 혼자 탐
        else:
            q.pop()
            total += 1
            
    return total
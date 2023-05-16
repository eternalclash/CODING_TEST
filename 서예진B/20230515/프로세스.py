from collections import deque

def solution(priorities, location):
    answer = 0
    n = len(priorities)
    q = deque()
    
    # 각 프로세스가 몇 번째로 실행되었는지 담을 배열 turn
    turn = [0 for _ in range(n)]
    # deque에 각 프로세스의 원래 순서, 우선순위 형태로 append 
    for i in range(n):
        q.append([i, priorities[i]])
    
    # 몇 번째로 프로세스가 실행되고 있는지 카운팅 
    cnt = 0
    while q:
        loc, p = q.popleft()
        # popleft 한 프로세스가 실행되었는지의 여부
        pick = True
        # deque를 순회하며 현재 프로세스보다 더 높은 우선순위를 가진 프로세스가 있는지 탐색
        for i in range(len(q)):
            if p < q[i][1]:
                # 있다면, 다시 deque의 맨 뒤에 넣고 pick 변수 false
                q.append([loc, p])
                pick = False
                break
        # 현재 프로세스보다 높은 우선순위가 없다면 cnt + 1
        if pick:
            cnt += 1
        
        # 해당 프로세스의 순번에 cnt 대입
        turn[loc] = cnt
    
    return turn[location]
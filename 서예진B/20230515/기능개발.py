from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    l = len(progresses)
    # 완료까지 필요한 작업일 수를 저장할 deque
    due = deque(0 for _ in range(l))
    # 각 기능마다 순회하며
    # 작업일 계산, 나누어떨어지지 않으면 + 1일 (올림 함수 이용)
    for i in range(l):
        remain = 100 - progresses[i]
        due[i] = math.ceil(remain / speeds[i])
    
    # 기준 작업일을 앞부터 pop
    start = due.popleft()
    cnt = 1
    while len(due) > 0:
        nex = due.popleft()
        # 앞 작업일보다 뒤의 작업일이 더 작으면 기다렸다가 함께 배포하므로
        # 총 기능 수 + 1
        if start >= nex:
            cnt += 1
        # 앞 작업일이 뒤의 작업일보다 크면 배포
        else:
            answer.append(cnt)
            # 기능 개수와 기준 작업일 초기화
            cnt = 1
            start = nex
            
    # 마지막 배포까지 append 해주기        
    answer.append(cnt)
    return answer
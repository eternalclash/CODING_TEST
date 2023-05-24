def solution(n, lost, reserve):
    answer = 0
    # 학생별 보유 체육복 수를 담은 배열 res
    res = [1 for _ in range(n)]
    # 여벌 체육복 + 1
    for idx in reserve:
        res[idx-1] += 1
    # 도난 체육복 - 1
    for idx in lost:
        res[idx-1] -= 1
    
    # 체육복 수를 순회하며
    for i in range(n):
        # 체육복이 없다면
        if res[i] == 0:
            # 양 옆 번호 학생들 체육복 수 조사
            # 첫번째 학생이면 두번째 학생만 확인
            if i == 0:
                if res[i+1] > 1:
                    res[i+1] -= 1
                    res[i] = 1
            # 양쪽 학생 모두 확인
            elif 1 <= i < n-1:
                if res[i-1] > 1:
                    res[i-1] -= 1
                    res[i] = 1
                elif res[i+1] > 1:
                    res[i+1] -= 1
                    res[i] = 1
            # 마지막 학생이면 바로 앞 학생만 확인
            elif i == n-1:
                if res[i-1] > 1:
                    res[i-1] -= 1
                    res[i] = 1
    # 체육복 수를 순회하며        
    for cnt in res:
        # 체육복이 0보다 크면 수업에 참여 가능
        if cnt > 0:
            answer += 1
            
    return answer
def solution(prices):
    n = len(prices)
    # 떨어지지 않은 기간을 세는 배열
    answer = [0 for _ in range(n)]
    for i in range(n):
        num = prices[i]
        for j in range(i+1, n):
            # 현재 가격보다 뒤의 가격들이 더 크면 기간 + 1
            if num <= prices[j]:
                answer[i] += 1
                
            # 현재 가격보다 작은 가격이 발견되면
            # 똑같이 기간 + 1, but 떨어졌기 때문에 break 해서 더 이상 카운팅 하지 않음
            else:
                answer[i] += 1
                break
    # 근데 이제 이 문제를 스택/큐를 써서 어떻게 풀까요 ..?
    return answer
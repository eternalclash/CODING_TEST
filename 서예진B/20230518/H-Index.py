def solution(citations):
    answer = 0
    n = len(citations)
    # h를 논문 개수로 초기화
    h = n
    
    # h를 줄여가며 h의 값이 적절한지 체크
    # O(n^2)인데 n이 1000이라서 가능
    while h >= 0:
        cited = 0
        less_cited = 0
        # citations 배열을 순회하며 논문 개수 카운팅
        for i in range(n):
            if citations[i] >= h:
                # h번 이상 인용된 논문 수 + 1
                cited += 1
            elif citations[i] <= h:
                # h번 이하로 인용된 논문 수 + 1
                less_cited += 1
                
        # h번 인용된 논문 수가 h개 이상, 나머지(n-cited)가 h번 이하로 인용
        if cited >= h and less_cited == n - cited:
            return h
    
        h -= 1
    '''
    엄청난 사람의 코드 ..
    
    citations.sort()
    for i in range(n):
        if citations[i] >= n - i:
            answer += 1
    '''
    return answer
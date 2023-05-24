def solution(answers):
    answer = []
    n = len(answers)
    
    # 1번 사람 12345
    ans1 = [1,2,3,4,5]
    score1 = 0
    # 정답 배열 순회하면서 5번씩 반복되므로 % 연산자 사용 
    for i in range(n):
        if ans1[i%5] == answers[i]:
            score1 += 1
    
    # 2번 사람 21232425
    ans2 = [2,1,2,3,2,4,2,5]
    score2 = 0
    for i in range(n):
        if ans2[i%8] == answers[i]:
            score2 += 1
    
    # 3번 사람 3311224455
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    score3 = 0
    for i in range(n):
        if ans3[i%10] == answers[i]:
            score3 += 1
            
    scores = [score1, score2, score3]
    max_score = max(scores)
    # 가장 높은 점수를 받은 사람 찾기, 오름차순으로 넣기 
    for i in range(3):
        if max_score == scores[i]:
            answer.append(i+1)
            
    return answer
def solution(answers):

    length = len(answers)
    answer1 = []
    answer2 = []
    answer3 = []

    # answers의 길이 이상이 될 때까지 수포자 1,2,3이 찍는 방식 반복해서 추가
    while len(answer1) <= length:
        answer1 += [1, 2, 3, 4, 5]

    while len(answer2) <= length:
        answer2 += [2, 1, 2, 3, 2, 4, 2, 5]

    while len(answer3) <= length:
        answer3 += [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # answers의 길이만큼 자르기
    answer1 = answer1[0:length]
    answer2 = answer2[0:length]
    answer3 = answer3[0:length]

    answersheet = [[], [], [], []]

    # 정답 개수만큼 정답지에 맞은 개수 추가
    for i, v in enumerate(answers):
        if answer1[i] == v:
            answersheet[1].append(1)
        if answer2[i] == v:
            answersheet[2].append(1)
        if answer3[i] == v:
            answersheet[3].append(1)

    table = [0, 0, 0, 0]

    # 수포자 1,2,3의 맞은 개수 총합 구하기
    table[1] = sum(answersheet[1])
    table[2] = sum(answersheet[2])
    table[3] = sum(answersheet[3])

    # 가장 높은 점수 구하기
    max_num = max(table)

    # 높은 점수를 받은 사람 answer에 추가
    answer = [i for i, v in enumerate(table) if v == max_num]

    print(answer)

    return answer

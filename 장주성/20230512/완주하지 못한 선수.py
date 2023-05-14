def solution(participant, completion):
    answer = ''
    dictionary = {}
    for person in participant:     # 참가자 리스트를 순회하며 이름과 등장 횟수를 딕셔너리에 저장
        if person in dictionary:
            dictionary[person] += 1
        else:
            dictionary[person] = 1
    for i in completion:     # 완주자 리스트를 순회하며 딕셔너리에서 해당 이름의 등장 횟수를 1씩 감소
        dictionary[i] -= 1

    for key, val in dictionary.items():     # 딕셔너리를 순회하며 등장 횟수가 1인 참가자를 찾아 결과값으로 설정
        if val == 1:
            answer = key

    return answer

def solution(participant, completion):
    answer = ''
    # 참가자 이름을 키로 하고, 인원을 값으로 하는 딕셔너리 선언
    p_dict = {}
    for ptct in participant:
        if ptct in p_dict:
            p_dict[ptct] += 1
        else:
            p_dict[ptct] = 1
    
    # 완주자 배열을 순회하며 딕셔너리의 값 - 1
    for c in completion:
        p_dict[c] -= 1
    
    # 완주하지 못했다면 딕셔너리의 값이 1 이상일 것
    for key, val in p_dict.items():
        if val != 0:
            # 완주하지 못한 사람은 1명이므로 찾자마자 return
            return key
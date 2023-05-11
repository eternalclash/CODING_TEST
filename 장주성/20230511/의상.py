def solution(clothes):
    answer = 0
    dictionary = {}

    for i in range(len(clothes)):
        if clothes[i][1] in dictionary:
            dictionary[clothes[i][1]].append(clothes[i][0])
        else:
            dictionary[clothes[i][1]] = [clothes[i][0]]

    clothes_num = len(dictionary)
    each_num = []

    for values in dictionary.values():
        each_num.append(len(values))

    while True:
        for i in each_num:
            answer += i
# 가능한 조합의 수 계산하는거에서 막힘
    return answer

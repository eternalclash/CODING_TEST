def solution(priorities, location):
    answer = 0
    arr = []
    max_num = max(priorities)
    while max_num != 0:
        for i, v in enumerate(priorities):
            if v == max_num:
                arr.append(v)
                priorities[i] = 0
            else:
                continue
    print(arr)
    print(priorities)

    return answer

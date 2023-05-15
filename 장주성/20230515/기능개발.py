def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)):
        num = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] > 0:
            num += 1
        arr.append(num)
    # progresses별 남은 일수 계산

    count = 0
    # index 계산을 위한 count 초기화

    max_num = arr[0]
    # 현재 끝내야 하는 최대 작업 일수 초기화

    answer.append(1)
    for j, v in enumerate(arr[1:]):
        if v <= max_num:
            answer[count] += 1
            # 다음에 올 작업 일수가 최대 작업 일수보다 작으면 count index에 추가
        else:
            answer.append(1)
            count += 1
            max_num = v
            # 더 큰 작업일수가 있으면 최대 작업 일수 변경

    return answer

def solution(n, lost, reserve):

    answer1 = 0
    answer2 = 0

    # n명의 체육복 개수 1개로 초기화
    array = [1] * (n+1)
    # 0번 인덱스는 사용하지 않으므로 0으로 초기화
    array[0] = 0

    # 체육복 잃어버린 사람은 0개로 변경
    for i in lost:
        array[i] = 0

    # 여분의 체육복 가지고 있는 사람은 체육복 추가
    for i in reserve:
        array[i] += 1

    array1 = array.copy()
    array2 = array.copy()

    # ###케이스 1번###
    # 이전 사람이 체육복 2개면 빌려오기
    for i, v in enumerate(array1):
        if i <= 1:
            continue
        if v == 0 and array1[i-1] == 2:
            array1[i] += 1
            array1[i-1] -= 1

    # 다음 사람이 체육복 2개면 빌려오기
    for i, v in enumerate(array1):
        if i == 0 or i == len(array1) - 1:
            continue
        if v == 0 and array1[i+1] == 2:
            array1[i] += 1
            array1[i+1] -= 1

    # 체육복 2개 이상인 사람 출력
    for i in array1[1:]:
        if i >= 1:
            answer1 += 1

    # ###케이스 2번###
    # 다음 사람이 체육복 2개면 빌려오기
    for i, v in enumerate(array2):
        if i == 0 or i == len(array2) - 1:
            continue
        if v == 0 and array2[i+1] == 2:
            array2[i] += 1
            array2[i+1] -= 1

    # 이전 사람이 체육복 2개면 빌려오기
    for i, v in enumerate(array2):
        if i <= 1:
            continue
        if v == 0 and array2[i-1] == 2:
            array2[i] += 1
            array2[i-1] -= 1

    # 체육복 2개 이상인 사람 출력
    for i in array2[1:]:
        if i >= 1:
            answer2 += 1

    # 케이스 1과 케이스 2 중에서 최댓값 출력
    answer = max(answer1, answer2)

    return answer

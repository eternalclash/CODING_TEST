from itertools import permutations

# 소수 찾는 함수 구현


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(numbers):

    answer = 0
    arr = list(numbers)
    array = []

    # 가능한 모든 조합 구현
    for j in range(1, len(arr)+1):
        for i in permutations(arr, j):
            array.append(''.join(i))

    # 중복 제거
    array = list(set(array))

    # 앞에 0으로 시작하는 수 제거
    for i, v in enumerate(array):
        array[i] = v.lstrip('0')

    # 빈 값 제거
    array = list(filter(None, array))
    array = list(set(array))

    # 1 제거
    if '1' in array:
        array.remove('1')

    # 소수면 answer에 추가
    for i, v in enumerate(array):
        if isPrime(int(v)) == True:
            answer += 1
    return answer

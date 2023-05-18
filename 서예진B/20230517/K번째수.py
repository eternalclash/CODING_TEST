def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        # i번째 ~ j번째 수를 담은 배열 num (인덱싱 : array[시작인덱스:끝인덱스+1])
        num = array[i-1:j]
        num.sort()
        # k번째 수를 answer 배열에 append
        answer.append(num[k-1])
    return answer
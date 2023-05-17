def solution(array, commands):
    answer = []
    arr = []
    for i in commands:
        arr = array[i[0]-1:i[1]]
        arr.sort()

        answer.append(arr[i[2]-1])

    return answer

def solution(arr):
    answer = []
    answer.append(arr[0])
    # 첫번째 배열의 index 추가
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])
        # 배열에서 서로 다른 값이 나올 때 마다 새로운 값 추가
    return answer

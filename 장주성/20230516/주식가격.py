def solution(prices):
    answer = []
    arr = []
    for i, v in enumerate(prices[:-1]):
        arr.append(prices[i+1]-prices[i])

    length = len(prices) - 1
    for i, v in enumerate(prices):
        answer.append(length - i)

    result = []

    for i, v in enumerate(arr):
        result.append(sum(arr[i:]))

    for i, v in enumerate(result):
        if v <= 0:
            answer[i] -= (v+1)

    return answer

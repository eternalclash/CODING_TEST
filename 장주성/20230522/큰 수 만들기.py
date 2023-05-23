def solution(number, k):
    answer = ''

    array = list(number)
    stack = [array[0]]  # 가장 큰 수를 찾기 위한 스택

    for num in array[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # 스택의 top이 현재 숫자보다 작으면 top을 제거하여 더 큰 숫자를 만듬
            stack.pop()
            k -= 1
        stack.append(num)

# k가 남아있는 경우, 가장 큰 숫자를 구성하는 숫자들 중 뒷부분을 제거
    if k > 0:
        stack = stack[:-k]

    answer = ''.join(stack)
    return answer

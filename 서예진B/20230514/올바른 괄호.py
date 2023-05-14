def solution(s):
    answer = True
    
    stack = list(s)
    # 여는 괄호와 닫는 괄호 개수 카운팅
    close = 0
    opening = 0
    last = stack.pop()
    # 마지막 괄호가 여는 괄호이면 올바르지 않은 괄호
    if last == '(':
        return False
    else:
        close += 1
    
    while len(stack) > 0: 
        if stack.pop() == '(':
            opening += 1
            # 현재까지의 닫는 괄호보다 여는 괄호가 더 많아지면 올바르지 않은 괄호
            if opening > close:
                return False
        else:
            close += 1
    # 모든 괄호의 개수를 카운팅 한 후, 여는 괄호와 닫는 괄호의 개수가 같으면 올바른 괄호
    if close == opening:
        return True
    # 그렇지 않으면 올바르지 않은 괄호
    else:
        return False
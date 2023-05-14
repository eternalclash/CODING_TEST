def solution(s):
    if s[0] == ')':
        return False
    # ')'로 시작하면 False

    opening_count = 0
    # 여는 괄호 개수 초기화

    for i in s:
        if i == '(':
            opening_count += 1
        # 여는 괄호 추가될 때마다 카운트 +1
        else:
            opening_count -= 1
        # 닫는 괄호는 카운트 -1
        if opening_count < 0:
            return False
        # 여는 괄호의 개수가 음수이면 False

    if opening_count > 0:
        return False
    # 전 과정이 끝난 후에 괄호의 개수가 양수이면 False

    return True

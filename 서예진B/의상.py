def solution(clothes):
    answer = 1
    # 의상의 종류를 키로 하는 딕셔너리 
    d = {}
    for name, category in clothes:
        if category in d:
            d[category].append(name)
        else:
            d[category] = [name]
    
    # 총 경우의 수는 카테고리별 의상을 선택하는 경우의 수를 곱한 총합
    for val in d.values():
        l = len(val)
        answer *= l + 1  
        # (l+1)을 곱하는 이유 : 해당 카테고리 중 아무것도 선택하지 않는 경우 포함
            
    return answer - 1
    # 아무것도 착용하지 않은 경우 빼기
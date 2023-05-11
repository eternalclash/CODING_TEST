def solution(nums):
    answer = 0
    n = len(nums)
    
    # 폰켓몬의 종류번호에 따른 수를 저장하기 위한 딕셔너리 선언
    mon = {}
    for num in nums:
        if num in mon:
            mon[num] += 1
        else:
            mon[num] = 1
    
    # 선택되는 폰켓몬의 수를 카운팅 하기 위한 변수 cnt
    cnt = 0
    # 선택되는 폰켓몬의 번호와 개수를 담은 딕셔너리 kind
    kind = {}
    
    for key, val in mon.items():
        if key in kind:  # 이미 선택된 번호라면
            kind[key] += 1  # 개수 + 1
        else:  # 처음 선택된 번호라면
            kind[key] = 1  # 개수 1로 설정
        cnt += 1
        
        # 종류별로 선택하다 n//2개가 되는 시점에 break
        if cnt == n//2:
            break
            
    return len(kind)
def solution(phone_book):
    answer = True
    # dictionary 선언한 이유 : 전화번호부에 있는 전화번호의 수(N)가 10^6이기 때문에
    # 리스트를 이용하면 이중 for 문으로 구현해야 하기 때문에 시간 초과남 O(N^2)
    prefix = dict()
    for num in phone_book:
        prefix[num] = 0  # 딕셔너리 사용 위해 무의미한 value(0) 넣기
    
    for num in prefix.keys():
        for i in range(1, len(num)):  # 전화번호 자신보다 짧은 문자열만
            if num[:i] in prefix:  # 문자열 슬라이싱 s[a:b] : O(b-a), 딕셔너리의 in : O(1)
                return False
            
    return answer
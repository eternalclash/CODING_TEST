def solution(phone_book):
    answer = True
    obj = {}
    for x in phone_book:
        obj[x] = 0
    for i in obj :
        for j in range(len(i)):
            if (i[:j] in obj) :
                return False
            
    return answer



# 파이썬 쉽지 않네;;
# obj로 해쉬화 한다음에 
# 반대로 오히려 긴 문자열에서 짧은 문자열을 찾는다
# obj 반복하면서  키 값 존재하면 리턴 False
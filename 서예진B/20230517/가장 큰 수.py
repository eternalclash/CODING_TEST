def solution(numbers):
    answer = ''
    ar = []
    # num은 최대 4자리수
    for num in numbers:
        # 각 숫자를 4번 반복해서 앞에서부터 4글자 슬라이싱
        '''
        처음에는 맨앞자리 수를 4자리가 될 때까지 채우면 되는 줄
        근데 만약 ['30', '303'] 이라면 '3033', '3033'이 되고
        만들 수 있는 가장 큰 수는 30330임 (30303보다 큼)
        그래서 '303'이 '30'보다 먼저 와야하는데 '3033'으로 같으므로 원하는대로 정렬 불가능
        '''
        tmp = (str(num) * 4)[:4]
        l = len(str(num))
        # ar배열에 변형시킨 문자열과 원래 문자열의 길이 저장
        ar.append((tmp, l))
        
    # 내림차순으로 정렬
    ar.sort(reverse=True)
    
    for (tmp, l) in ar:
        # 원래 문자열의 길이만큼 answer에 더해줌
        answer += tmp[:l]
        
    # answer의 결과가 int일 때 0이라면 ('00', '000','0000')
    if int(answer) == 0:
        # '0' 리턴
        return '0'
    
    return answer
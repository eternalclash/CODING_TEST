# 순열 함수, n : 뽑는 개수, 순열 경우의 수를 담은 2차원 배열 반환
def perm(arr, n):
    result = []
    if n > len(arr):
        return result
    # 1개를 뽑으므로 arr을 순회하며 배열에 추가
    if n == 1:
        for i in arr:
            result.append([i])
    
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                result.append([arr[i]]+p)
    
    return result


def solution(numbers):
    answer = 0
    # 길이가 최대 7자이므로 limit을 10**7로 설정
    limit = 10 ** 7
    # num : 소수임을 판별하기 위한 배열, 0과 1은 소수가 아니므로 False
    num = [True for _ in range(limit)]
    num[0] = False
    num[1] = False
    
    # i를 2부터 시작해서 limit-1까지
    for i in range(2, limit):
        # i가 소수이면
        if num[i]:
            # i*2부터 시작해서 limit 전까지 i씩 더해지는 수는 소수가 아님
            idx = 2 * i
            while idx < limit:
                num[idx] = False
                idx = idx + i
    
    # numbers에 있는 문자를 int형으로 한 글자씩 저장
    arr = []
    for number in numbers:
        arr.append(int(number))
    
    l = len(numbers)
    # 소수의 중복 카운팅 방지를 위해 prime 배열 선언
    prime = []
    # 뽑는 수를 1부터 l까지 반복하며
    for i in range(1, l+1):
        # 만들 수 있는 숫자의 경우의 수를 모두 구함
        perm_list = perm(arr, i)
        for case in perm_list:
            # 배열 안의 숫자를 문자열로 합침
            case_string = ""
            for digit in case:
                case_string += str(digit)
            # 맨 앞자리 문자가 0이면 int형으로 변환할 수 없으므로 0 제거
            # but 진짜 0은 제거하면 안됨
            if case_string[0] == '0' and len(case_string) > 1:
                case_string = case_string[1:]
            case_int = int(case_string)
            # case_int가 소수인지 판별
            if num[case_int]:
                # 이미 카운팅 한 소수라면 continue
                if case_int in prime:
                    continue
                # 아니라면 prime에 추가 후 개수 + 1
                else:
                    prime.append(case_int)
                    answer += 1
                
    return answer
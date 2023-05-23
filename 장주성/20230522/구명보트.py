def solution(people, limit):
    answer = 0
    people.sort()
    # 가장 가벼운 사람 인덱스
    light = 0
    # 가장 무거운 사람 인덱스
    heavy = len(people) - 1

    while light <= heavy:
        # 가장 가벼운 사람과 무거운 사람의 몸무게 합
        total_weight = people[light] + people[heavy]
        if total_weight <= limit:
            # 같이 태울 수 있으면 같이 태우고 인덱스 업데이트
            light += 1
            heavy -= 1
        else:
            # 못태우면 무거운 사람만 태우기
            heavy -= 1

        # 구명보트 개수 증가
        answer += 1

    return answer

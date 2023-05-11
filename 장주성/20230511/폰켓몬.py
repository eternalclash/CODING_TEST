def solution(nums):
    answer = 0
    counts = {}

    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    # 입력으로 주어진 배열을 폰켓몬 종류별로 분류하고, 폰켓몬 종류 별 폰켓몬 수를 구함

    half = len(nums) / 2
    # 최대로 가져갈 수 있는 N/2마리의 포켓몬 수

    if len(counts) >= half:
        answer = half
    else:
        answer = len(counts)
    # 가져갈 수 있는 폰켓몬 수가 N/2마리 이상이면 N/2마리 가져감
    # 그보다 적으면, 가져갈 수 있는 폰켓몬만 가져감

    return answer

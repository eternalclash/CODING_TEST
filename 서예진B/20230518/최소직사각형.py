def solution(sizes):
    answer = 0
    l = len(sizes)
    # 가로와 세로 중 짧은 변을 항상 가로로 하면 최소 지갑 크기 구할 수 있음
    
    # 명함 사이즈 배열을 순회하면서
    # 가로 길이보다 세로 길이가 더 길면, 가로 길이와 세로 길이 바꿈
    for i in range(l):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    
    # 가로 길이 중 가장 긴 길이 탐색 
    max_width = sizes[0][0]
    for i in range(1, l):
        if max_width < sizes[i][0]:
            max_width = sizes[i][0]
    
    # 세로 길이 중 가장 긴 길이 탐색
    max_height = sizes[0][1]
    for i in range(1, l):
        if max_height < sizes[i][1]:
            max_height = sizes[i][1]
            
    # 답은 가로 max * 세로 max
    answer = max_width * max_height
    return answer
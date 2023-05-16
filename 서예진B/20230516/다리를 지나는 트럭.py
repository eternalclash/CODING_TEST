from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque(0 for _ in range(bridge_length))
    truck_weights = deque(truck_weights)
    
    # 현재 다리에 있는 트럭의 총 무게
    tw = 0
    # 모든 트럭이 다리에 올라갈 때까지
    while truck_weights:
        answer += 1
        # 1. 다리에 있는 모든 트럭들은 앞으로 한 칸씩 이동한다. 
        # (다리의 맨 앞에 있는 트럭이 다리를 완전히 지난다)
        # 그러므로 tw에서 그 무게만큼 차감
        tw -= bridge.popleft()
        '''
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft()
        처음에는 sum 함수를 이용해서 계속해서 다리 위 트럭 무게합을 구함
        그렇게 하면 매번 O(n)의 시간이 걸리기 때문에 비효율적 -> 시간 초과 (케이스5)
        '''
        # 현재 다리 위의 총 트럭 무게와 맨 앞 대기 트럭의 무게 합이 무게 제한보다 작으면
        # 다리에 올라갈 수 있다
        if tw + truck_weights[0] <= weight:
            w = truck_weights.popleft()
            # 다리에 추가
            bridge.append(w)
            # 다리 위 트럭 무게 총합에 더해주기
            tw += w
        # 무게 제한보다 커서 트럭이 올라가지 못하면 0 추가
        else:
            bridge.append(0)
    
    # 모든 트럭이 다리 위에 올라갔을 때, 다리 위의 트럭은
    # 가장 뒤에 있는 트럭이 다리를 완전히 통과하면 끝
    # bridge를 순회하며 맨 뒤의 트럭 인덱스를 구함
    last = 0
    for i in range(bridge_length):
        if bridge[i] > 0:
            last = i
            
    # 걸린 시간은 마지막 트럭 인덱스 + 1
    answer += last + 1

    return answer
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    count = 0
    waiting = []

    for i in truck_weights:
        waiting.append([i, bridge_length])

    bridge.append(waiting[0])
    waiting[0][1] -= 1
    count += 1

    for i, v in enumerate(waiting[1:]):

        result = 0
        for i in bridge:
            result += i[0]

        if (result + v[0]) <= weight:
            bridge.append(v)

        for j in bridge:
            j[1] -= 1

        if v[1] == 0:
            bridge.remove(v)

    count += 1

    return answer

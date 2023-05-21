def solution(name):
    alphabet = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 12,
        'P': 11,
        'Q': 10,
        'R': 9,
        'S': 8,
        'T': 7,
        'U': 6,
        'V': 5,
        'W': 4,
        'X': 3,
        'Y': 2,
        'Z': 1
    }
    answer = 0
    for i in name:
        answer += alphabet[i]

    num_a = 0
    num_a_reverse = 0
    isA = True
    isA_reverse = True

    while isA:
        for i in name[1:]:
            if i == 'A':
                num_a += 1
            else:
                isA = False
                break
        if not isA:
            break

    while isA_reverse:
        for i in name[-1:0:-1]:
            if i == 'A':
                num_a_reverse += 1
            else:
                isA_reverse = False
                break
        if not isA_reverse:
            break

    answer += (len(name)-1)
    answer = answer - num_a - num_a_reverse

    return answer

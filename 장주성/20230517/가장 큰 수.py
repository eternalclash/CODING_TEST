def solution(numbers):
    answer = ''
    string = []
    test = [[] for i in range(10)]

    for i in numbers:
        string.append(str(i))

    string.sort()

    for i in string[::-1]:
        index = int(i[0])

        test[index].append(i)

    for i in test:
        if len(i) == 0:
            continue

        # for j in i:
        #     max_val = max(len(j))
        #     print(max_val)

    return answer

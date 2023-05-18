def solution(citations):
    answer = 0
    avg = sum(citations) / len(citations)
    citations.sort(reverse=True)
# #     arr = [[] for i in range(max(citations))]

#     for i in range(max(citations)):
#         for j in citations:
#             if j > i:

#     print(arr)
    for i in range(len(citations)):
        citations[i]

    # print(citations)
    # print(int(len(citations) / 2) - 1)
#     for i, v in enumerate(citations):
#         citations[i] -= avg

#     answer = 0
#     for i in citations:
#         if i >= 0:
#             answer += 1

    answer = int(avg)

    return answer

# 풀다 포기!!!

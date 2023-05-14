def solution(phone_book):
    answer = True
    for i, v in enumerate(phone_book):
        phone_book[i] = int(v)
    phone_book.sort()
    for i, v in enumerate(phone_book):
        phone_book[i] = str(v)

    for i, v in enumerate(phone_book):
        for j, k in enumerate(phone_book[i+1:]):
            if v in k:
                return False

    return True

# 오답

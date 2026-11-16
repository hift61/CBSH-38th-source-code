N = int(input())

l = []
for _ in range(N):
    # rstrip() : 오른쪽에 있는 시퀀스 제거
    tmp = input().rstrip()

    # pop(n) : n번째 인덱스의 값을 제거 (del()과  유사)
    if len(tmp) == 3:
        l.pop(-1)
    else:
        order, num = tmp.split()

        l.append(num)

# if문의 조건에 리스트를 넣으면, 길이가 0인 경우에 거짓
if l:
    print(*l)
else:
    print("EMPTY")
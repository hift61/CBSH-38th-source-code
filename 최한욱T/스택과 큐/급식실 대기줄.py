N = int(input())

l = []
flag = True
for _ in range(N):
    tmp = input().rstrip()

    if len(tmp) == 5:
        print(l.pop(0))

        flag = False
    else:
        order, num = tmp.split()

        l.append(num)

if flag:
    print("NONE")
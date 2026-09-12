N = int(input())
Ns = list(map(int, input().split()))

last_num = Ns.pop(0)
re = [last_num]
for _ in range(N - 1):
    tmp = Ns.pop(0)

    if tmp != last_num:
        last_num = tmp
        re.append(last_num)

print(*re, sep = ' ')
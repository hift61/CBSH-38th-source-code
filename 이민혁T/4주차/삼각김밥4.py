N = int(input())

re = 0
if N >= 3:
    for c in range(N // 3, N // 2 + 1):
        for b in range(1, c + 1):
            a = N - b - c

            if 1 <= a <= b <= c:
                re += 1

    print(re)
else:
    print(0)
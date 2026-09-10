L, VA, VB, D = map(int, input().split())

if (L - D) % (VA + VB) == 0:
    print((L-D) // (VA + VB))
else:
    print((L - D) // (VA + VB) + 1)
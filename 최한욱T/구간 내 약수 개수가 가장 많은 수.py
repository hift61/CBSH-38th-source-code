N = int(input())
re = [0, -1 * float('inf')]

for i in range(1, N + 1):
    c = 0

    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
    
    if c > re[1]:
        re = [i, c]

print(*re, sep = ' ')

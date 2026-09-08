N, M = map(int, input().split())

re = [0, 0] 
for n in range(N):
    s = input().rstrip().split()

    l_word = s[0]
    tmp = 1
    for c in s[1:]:
        if c == l_word:
            tmp += 1
        else:
            if tmp > re[1]:
                re = [n + 1, tmp]

            tmp = 1
            l_word = c
    
    if tmp > re[1]:
        re = [n + 1, tmp]

print(*re, sep = ' ')

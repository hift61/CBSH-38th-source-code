N = int(input())
    
s, e = 1, 1
cs = 1
re = 0

while s <= N:
    if cs == N:
        re += 1
        cs -= s
        s += 1
    elif cs < N:
        e += 1
        cs += e
    else:
        cs -= s
        s += 1

print(re * 2)

# 제가 별찍기가 좀 약합니다 ㅎ

import sys
sys.setrecursionlimit(10**5)

def answer(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    
    tmp = answer(n // 2)

    top = [" " * (n // 2) + s + " " * (n // 2) for s in tmp]
    bottom = [s + " " + s for s in tmp]

    return top + bottom

N = int(input())
for l in answer(N):
    print(l.rstrip())
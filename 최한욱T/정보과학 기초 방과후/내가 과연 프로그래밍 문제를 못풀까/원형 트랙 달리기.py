from math import gcd

L, VA, VB = map(int, input().split())

if L % (VA - VB) == 0:
    print(f"{L // (VA - VB)}/{1}")
else:
    tmp = gcd(L, VA - VB)

    print(f"{L // tmp}/{(VA - VB) // tmp}")
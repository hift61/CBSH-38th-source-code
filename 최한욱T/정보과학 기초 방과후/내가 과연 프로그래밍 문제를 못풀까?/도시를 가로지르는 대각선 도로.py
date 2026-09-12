from math import gcd

N, M = map(int, input().split())

print(N + M - gcd(N, M))
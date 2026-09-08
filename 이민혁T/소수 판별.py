from sys import exit

N = int(input())

for i in range(2, N // 2 + 1):
    if N % i == 0:
        print("not prime")
        exit()

print("prime")

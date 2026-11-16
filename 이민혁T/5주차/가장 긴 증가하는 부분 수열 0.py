def answer(idx, LIS):
    if idx == N:
        return len(LIS)

    if not LIS or LIS[-1] < Ns[idx]:
        tmp = LIS + [Ns[idx]]
        return max(answer(idx + 1, LIS), answer(idx + 1, tmp))
    else:
        return answer(idx + 1, LIS)

N = int(input())
Ns = list(map(int, input().split()))

print(answer(0, []))
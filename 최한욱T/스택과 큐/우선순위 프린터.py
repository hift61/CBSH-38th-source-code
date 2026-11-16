def find_max_value(arr):
    max_value = arr[0]
    for i in range(1, len(arr)):
        if max_value < arr[i]:
            max_value = arr[i]
    return max_value

N, M = map(int, input().split())
Ns = list(map(int, input().split()))

queue = list(enumerate(Ns))

cnt = 0
while queue:
    idx, value = queue.pop(0)

    if value >= find_max_value(Ns):
        cnt += 1
        Ns.remove(value)

        if idx == M:
            print(cnt)
            break
    else:
        queue.append((idx, value))
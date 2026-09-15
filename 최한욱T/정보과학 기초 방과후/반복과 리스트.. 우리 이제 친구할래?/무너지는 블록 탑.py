N = int(input())
HN = list(map(int, input().split()))

last_block = [HN[0]]
for i in HN[1:]:
    if i >= last_block[-1]:
        last_block.append(i)

print(*last_block, sep = ' ')
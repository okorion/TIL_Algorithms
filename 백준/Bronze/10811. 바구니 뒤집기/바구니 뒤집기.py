import sys
input = sys.stdin.readline

N, M = map(int, input().split())

baguni = [x for x in range(1, N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    bagu = reversed(baguni[start - 1:end])
    # print(baguni[:start - 1], list(bagu), baguni[end:])
    # print('?', list(bagu))

    baguni = baguni[:start - 1] + list(bagu) + baguni[end:]

print(*baguni)


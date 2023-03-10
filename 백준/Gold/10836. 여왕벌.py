import sys

input = sys.stdin.readline

M, N = map(int, input().split())

matrix = [[1] * M for _ in range(M)]
li = [1] * (2 * M - 1)

for _ in range(N):
    t_list = list(map(int, input().split()))
    temp_list = []

    for idx, val in enumerate(t_list):  #input 형태 변환, 1 1 1 -> [0, 1, 2] / 0 3 0 -> [1, 1, 1]
        temp_list += [idx] * val
    for _ in range(2*M-1):
        li[_] += temp_list[_]


half = (2 * M - 1) // 2
A = li[half + 1:]
for i in range(half, -1, -1):
    print(li[i], end=" ")
    for a in A:
        print(a, end=" ")
    print()

import sys
input = sys.stdin.readline

K, N = map(int, input().split())

wire_list = []

for _ in range(K):
    wire_list.append(int(input()))

start = 1
end = max(wire_list)

while start <= end:
    mid_answer = (start + end) // 2
    line = 0

    for _ in wire_list:
        line += _ // mid_answer

    if line >= N:
        start = mid_answer + 1
    elif line < N:
        end = mid_answer - 1

print(end)

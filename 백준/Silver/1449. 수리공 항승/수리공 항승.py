import sys
input = sys.stdin.readline

N, L = map(int, input().split())
tape_list = list(map(int, input().split()))

tape_list.sort()

start = tape_list[0] - 0.5
end = tape_list[0] + L
cnt = 1

for _ in range(N):
    if start < tape_list[_] < end:
        continue
    else:
        start = tape_list[_] - 0.5
        end = tape_list[_] + L
        cnt += 1

print(cnt)

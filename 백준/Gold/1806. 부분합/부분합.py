import sys

input = sys.stdin.readline

N, S = map(int, input().split())

temp_list = list(map(int, input().split()))

start = 0
end = 0
answer = float("inf")
tmp_sum = 0

# print(temp_list)

while True:
    if tmp_sum >= S:
        answer = min(answer, end - start)
        tmp_sum -= temp_list[start]
        start += 1

    elif end == N:
        break

    elif tmp_sum < S:
        tmp_sum += temp_list[end]
        end += 1

    # print(start, end)

if answer == float("inf"):
    print(0)
else:
    print(answer)

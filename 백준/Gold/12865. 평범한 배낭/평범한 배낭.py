import sys

input = sys.stdin.readline

N, K = map(int, input().split())
temp_result = [0] * (K + 1)
temp_pair = []

for _ in range(N):
    temp_pair.append(list(map(int, input().split())))

# print(temp_pair)
# print(temp_result)

for _ in temp_pair:
    for val in range(K):
        if _[0] <= K-val:
            temp_result[-val-1] = max(temp_result[-val-1], _[1] + temp_result[-val-1 - _[0]])

print(temp_result[-1])

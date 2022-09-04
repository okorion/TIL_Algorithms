import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split())) + [0]
temp_list = [0]
num = 0

for _ in range(N):
    num += num_list[_]
    temp_list.append(num)
    
for n in range(M):
    a, b = map(int, input().split())
    result = temp_list[b] - temp_list[a-1]
    print(result)
    
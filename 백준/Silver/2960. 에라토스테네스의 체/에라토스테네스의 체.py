import sys
input = sys.stdin.readline

N, K = map(int, input().split())

temp_list = [0] * (N+1)

# print(temp_list)
cnt = 0

for _ in range(2, N+1):    # 2,3,4,5,6,7
    for a in range(_, N+1, _):   # [2,4,6] [3,6] [4] ~ [7]
        if temp_list[a] == 0:
            temp_list[a] = 1
            cnt += 1
            if cnt == K:
                print(a)

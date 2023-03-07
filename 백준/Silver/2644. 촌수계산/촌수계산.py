import sys

input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
M = int(input())

temp_list = [[] for _ in range(N + 1)]

# print(temp_list)

for _ in range(M):
    a, b = map(int, input().split())

    temp_list[a].append(b)
    temp_list[b].append(a)

# print(temp_list)

visited = [0] * (N + 1)
result = False
num = 10e10
visited[A] = 1


def dfs(x, y, cnt):
    global result, num

    # print(x, y, cnt, visited)
    if x == y:
        # print("x==y")
        if cnt < num:
            result = True
            num = cnt
            return

    if temp_list[x]:
        for _ in temp_list[x]:
            if visited[_] == 0:
                visited[x] = 1
                # print(_, y, cnt+1, visited)
                dfs(_, y, cnt + 1)
                visited[x] = 0


dfs(A, B, 0)

if result:
    print(num)
else:
    print(-1)

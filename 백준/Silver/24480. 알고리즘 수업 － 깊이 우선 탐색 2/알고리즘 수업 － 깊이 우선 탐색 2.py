import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, R = map(int, input().split())
line_list = []
node = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
answer = [0] * (N + 1)
count = 1


def dfs(num):
    global count

    visited[num] = 1
    answer[num] = count

    node[num].sort(reverse=True)
    for n in node[num]:
        if visited[n] == 0:
            count += 1
            visited[n] = 1
            dfs(n)
            

for _ in range(M):
    x, y = map(int, input().split())
    node[x].append(y)
    node[y].append(x)

dfs(R)

for _ in range(1, N + 1):
    print(answer[_])

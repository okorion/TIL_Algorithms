import sys

input = sys.stdin.readline

N = int(input())
cnt = 0
visited = [0] * (N+1)


def queen(x, n):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n):
            visited[x] = i
            if check(x):
                queen(x+1, n)


def check(x):
    for i in range(x):
        if visited[i] == visited[x] or abs(visited[x]-visited[i]) == x-i:
            return False
    return True


queen(0, N)
print(cnt)

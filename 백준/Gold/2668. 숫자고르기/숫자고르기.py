import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N = int(input())

temp_list = [[] for _ in range(N + 1)]

for _ in range(1, N + 1):
    temp = int(input())
    temp_list[_].append(temp)


final_list = []


def dfs(x):
    nx = temp_list[x][0]
    visited_list.append(x)
    result_list.append(nx)

    if sorted(visited_list) == sorted(result_list):
        for t in result_list:
            final_list.append(t)
        return
    elif len(set(visited_list)) != len(set(result_list)):
        return

    dfs(nx)
    visited_list.pop()
    result_list.pop()


for _ in range(1, N + 1):
    visited_list = []
    result_list = []
    dfs(_)
    if temp_list[_][0] == _:
        final_list.append(_)

final_list.sort()
final_list = set(final_list)

print(len(final_list))
for _ in sorted(final_list):
    print(_)

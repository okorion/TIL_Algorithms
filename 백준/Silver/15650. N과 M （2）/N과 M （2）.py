import sys
input = sys.stdin.readline

N, M = map(int, input().split())

temp_list = []


def dfs():
    if len(temp_list) == M:
        print(" ".join(map(str, temp_list)))
        return

    for _ in range(1, N+1):
        if _ not in temp_list:
            if len(temp_list) == 0:
                temp_list.append(_)
                dfs()
                temp_list.pop()
            else:
                if _ > temp_list[-1]:
                    temp_list.append(_)
                    dfs()
                    temp_list.pop()


dfs()

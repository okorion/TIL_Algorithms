import sys
input = sys.stdin.readline

temp_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z'
    ]
string_list = list(input())
visited = [-1 for _ in range(26)]
cnt = 0

for _ in temp_list:
    if _ in string_list:
        visited[cnt] = string_list.index(_)
    cnt += 1

# print(temp_list)
# print(string_list)
print(*visited)

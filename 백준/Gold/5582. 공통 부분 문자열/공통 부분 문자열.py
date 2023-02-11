import sys
input = sys.stdin.readline

first_str = list(input().strip())
second_str = list(input().strip())

# print(first_str, second_str)

visited = [[0] * (len(first_str) + 1) for _ in range(len(second_str) + 1)]
# print(visited)

for i in range(1, len(first_str) + 1):
    for j in range(1, len(second_str) + 1):
        if first_str[i-1] == second_str[j-1]:
            visited[j][i] = visited[j-1][i-1] + 1
        # print(first_str[i], second_str[j], i, j)
# print(visited)
result = []

for _ in visited:
    result.append(max(_))

print(max(result))

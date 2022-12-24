N = int(input())
result = 0

A_list = list(map(int, input().split()))
A_list.sort()
B_list = list(map(int, input().split()))
B_list.sort(reverse=True)

for _ in range(N):
    result += A_list[_] * B_list[_]

print(result)

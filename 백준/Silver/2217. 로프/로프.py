N = int(input())
temp_list = []
result = 0

for _ in range(N):
    temp_list.append(int(input()))

temp_list.sort(reverse=True)

for _ in range(N):
    if temp_list[-_-1] * (N-_) > result:
        result = temp_list[-_-1] * (N-_)

print(result)

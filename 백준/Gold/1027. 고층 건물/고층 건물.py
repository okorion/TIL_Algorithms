import sys

input = sys.stdin.readline

N = int(input())

building_list = list(map(int, input().split()))

result = 0

for i in range(N):
    cnt = 0
    giulgi_left = -float('inf')
    giulgi_right = -float('inf')
    for left in range(i-1, -1, -1):
        if (building_list[left] - building_list[i])/(i - left) > giulgi_left:
            giulgi_left = (building_list[left] - building_list[i]) / (i - left)
            cnt += 1

    for right in range(i+1, N):
        if (building_list[right] - building_list[i])/(right - i) > giulgi_right:
            giulgi_right = (building_list[right] - building_list[i]) / (right - i)
            cnt += 1

    result = max(result, cnt)

print(result)

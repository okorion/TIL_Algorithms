import sys
input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))
ans = float('INF')
left, right = 0, 0
l = 0
r = N - 1

while l < r:
    tmp = temp_list[l] + temp_list[r]

    if abs(tmp) < ans:
        ans = abs(tmp)
        left = temp_list[l]
        right = temp_list[r]

    elif tmp > 0:
        r -= 1

    else:
        l += 1

print(left, right)

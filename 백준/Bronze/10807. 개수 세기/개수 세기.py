import sys
input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))
num = int(input())
cnt = 0

for _ in range(N):
    if temp_list[_] == num:
        cnt += 1
        
print(cnt)

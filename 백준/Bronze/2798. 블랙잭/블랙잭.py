import sys

N, M = map(int, sys.stdin.readline().split())

temp_list = list(map(int, sys.stdin.readline().split()))
res = 0

for i in range(len(temp_list)-2):
    for j in range(i+1,len(temp_list)-1):
        for k in range(j+1, len(temp_list)):
            tmp = temp_list[i] + temp_list[j] + temp_list[k]

            if res <= tmp <= M:
                res = tmp

print(res)

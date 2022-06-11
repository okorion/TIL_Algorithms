import sys

N, M = map(int, sys.stdin.readline().split())

temp_list = list(map(int, sys.stdin.readline().split()))
res = 0

for i in range(len(temp_list)-2):
    if temp_list[i] == temp_list[i-1]:
        continue
    for j in range(i+1,len(temp_list)-1):
        if j > i+1 and temp_list[j] == temp_list[j-1]:
            continue
        for k in range(j+1, len(temp_list)):
            if k > j+1 and temp_list[k] == temp_list[k-1]:
                continue
            tmp = temp_list[i] + temp_list[j] + temp_list[k]

            if res <= tmp <= M:
                res = tmp

print(res)

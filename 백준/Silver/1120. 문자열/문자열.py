import sys

input = sys.stdin.readline

A, B = map(list, input().split())

dif_num = len(B)-len(A)
cnt = 0
result_list = []

for k in range(dif_num+1):
    for i in range(len(A)):
        if A[i] == B[i+k]:
            cnt += 0
        else:
            cnt += 1
    result_list.append(cnt)
    cnt = 0

print(min(result_list))

import sys
input = sys.stdin.readline

N = int(input())

# 양수는 양수랑 곱하기, 1은 혼자, 0은 혼자 or 음수랑 합치기, 음수는 음수랑 곱하기

plus_list = []
one_list = []
zero_list = []
minus_list = []

for _ in range(N):
    x = int(input())

    if x > 1:
        plus_list.append(x)
    elif x == 1:
        one_list.append(x)
    elif x == 0:
        zero_list.append(x)
    elif x < 0:
        minus_list.append(x)

plus_list.sort(reverse=True)
minus_list.sort()

result = 0

# print(plus_list)
# print(one_list)
# print(zero_list)
# print(minus_list)

plus_sum = 0
minus_sum = 0

if not (len(plus_list) % 2):
    for _ in range(len(plus_list)//2):
        plus_sum += plus_list[_*2] * plus_list[_*2+1]
else:
    for _ in range(len(plus_list)//2):
        plus_sum += plus_list[_*2] * plus_list[_*2+1]
    plus_sum += plus_list[-1]


if not (len(minus_list) % 2):
    for _ in range(len(minus_list)//2):
        minus_sum += minus_list[_*2] * minus_list[_*2+1]
else:
    if not zero_list:
        for _ in range(len(minus_list)//2):
            minus_sum += minus_list[_*2] * minus_list[_*2+1]
        minus_sum += minus_list[-1]
    else:
        for _ in range(len(minus_list)//2):
            minus_sum += minus_list[_*2] * minus_list[_*2+1]


result = plus_sum + len(one_list) + minus_sum
# print(plus_sum)
print(result)

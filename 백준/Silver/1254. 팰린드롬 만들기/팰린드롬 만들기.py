import sys

input = sys.stdin.readline

temp = list(input().rstrip())

# print(temp)
# print(temp[::-1])
result = 0

for i in range(len(temp)):
    for j in range(len(temp[::-1])):
        if temp[i:-1] == temp[::-1][0:len(temp) - i - 1]:
            # print(temp[i:-1])
            # print(temp[0:len(temp) - i - 1])
            print(len(temp) * 2 - len(temp[i:-1]) - 1)
            quit(0)

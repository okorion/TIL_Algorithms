import sys

N = int(sys.stdin.readline())

stack = []
count = 1
test_list = []
result_list = []
temp = True

for x in range(N):
    test_list.append(int(sys.stdin.readline()))

for _ in range(N):
    while test_list[_] >= count:
        result_list.append('+')
        stack.append(count)
        count += 1

    # print(stack, result_list[_])
    if stack[-1] == test_list[_]:
        result_list.append('-')
        stack.pop()

    else:
        temp = False
        break

if not temp:
    print("NO")

else:
    for i in result_list:
        print(i)

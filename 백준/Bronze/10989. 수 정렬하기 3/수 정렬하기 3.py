import sys

# a = []    # 배열은 메모리를 많이 먹음.
#
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#     a.append(int(input()))
#
# a.sort()
#
# for _ in a:
#     print(_)

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
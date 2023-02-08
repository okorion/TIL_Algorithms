import sys

input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

# print(S, T)
flag = False

while True:
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T.reverse()
        # print(T)

    if T == S:
        flag = True
        break
    if not len(T):
        break

if flag:
    print(1)
else:
    print(0)

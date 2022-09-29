import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    temp_list = list(input().strip())
    stack = []
    cnt = 0

    for t in temp_list:
        if t == "(":
            stack.append("(")
            cnt += 1
            if len(temp_list) == cnt:
                print("NO")
                stack = []
                cnt = 0
                break
        elif t == ")":
            if len(stack) != 0:
                if stack[-1] == "(":
                    stack.pop()
                    cnt += 1
                    if len(temp_list) == cnt:
                        if len(stack) == 0:
                            print("YES")
                            stack = []
                            cnt = 0
                            break
                        else:
                            print("NO")
                            stack = []
                            cnt = 0
                            break
            else:
                print("NO")
                stack = []
                cnt = 0
                break


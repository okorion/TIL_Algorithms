import sys

input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))

if list(range(1, N + 1)[::-1]) == temp_list:
    print(-1)

else:
    # print(temp_list)
    for p in range(N - 1, -1, -1):
        # print(p)
        left, right = temp_list[:p], temp_list[p:]
        # print(left, right)

        if temp_list[p - 1] < temp_list[p]:
            tmp = temp_list[p - 1]
            # print(tmp)

            val = tmp + 1
            cnt = 1

            while True:   # val 값 확정시키기
                if val in left:
                    val += 1
                    cnt += 1
                elif val in right:
                    right[right.index(val)] = right[right.index(val)] - cnt
                    right.sort()
                    break

            print(*(left[:-1] + [val] + right))
            quit(0)



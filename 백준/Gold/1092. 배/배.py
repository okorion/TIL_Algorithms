import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
W = int(input())
W_list = list(map(int, input().split()))

N_list.sort(reverse=True)
W_list.sort(reverse=True)

time = 0

if N_list[0] < W_list[0]:
    print(-1)
    exit()

else:
    time = 0

    while W_list:
        if not W_list:
            break

        for i in N_list:
            for j in W_list:
                if i >= j:
                    W_list.remove(j)
                    break

        time += 1

print(time)

N = int(input())

total_y = 0
total_k = 0

for t in range(N):
    for _ in range(9):
        Y, K = map(int, input().split())
        total_y += Y
        total_k += K

    if total_k > total_y:
        print("Korea")
    elif total_k < total_y:
        print("Yonsei")
    else:
        print("Draw")
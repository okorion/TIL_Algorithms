import sys

M = int(sys.stdin.readline())
tempList_A = list(map(int, sys.stdin.readline().split()))
tempList_A.sort()

N = int(sys.stdin.readline())
tempList_B = list(map(int, sys.stdin.readline().split()))


def binary_search(var):
    start = 0
    end = M - 1

    while start <= end:             # while var <= tempList_A[mid]:
        mid = (start + end) // 2
        if var == tempList_A[mid]:
            return True
        elif var < tempList_A[mid]:
            end = mid - 1
        elif var > tempList_A[mid]:
            start = mid + 1


for _ in range(N):
    if binary_search(tempList_B[_]):
        print(1)
    else:
        print(0)



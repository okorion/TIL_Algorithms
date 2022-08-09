from collections import Counter
import sys

input = sys.stdin.readline


M = int(input())
templist_M = Counter(list(map(int, input().split())))

N = int(input())
templist_N = list(map(int, input().split()))

result = []

for n in range(N):
    if templist_N[n] in templist_M:
        result.append(templist_M[templist_N[n]])
    else:
        result.append(0)
 
print(*result)

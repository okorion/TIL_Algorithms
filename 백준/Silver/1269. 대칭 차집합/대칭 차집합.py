import sys
from collections import Counter

input = sys.stdin.readline

A, B = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

result = len(Counter(A_list) - Counter(B_list)) + len(Counter(B_list) - Counter(A_list))

print(result)


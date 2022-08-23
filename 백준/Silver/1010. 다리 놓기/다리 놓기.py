import sys
import math

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    a, b = map(int, input().split())
    result = (math.factorial(b)/math.factorial(b-a))/math.factorial(a)

    print(round(result))

import sys

input = sys.stdin.readline

array = [True for _ in range(1000001)]
array[0] = False
array[1] = False

for i in range(2, 1001):
    if array[i]:
        for j in range(i + i, 1000001, i):
            array[j] = False

temp = int(input())

while temp != 0:
    for _ in range(2, temp//2 + 1):
        if array[_] and array[temp-_]:
            print(f"{temp} = {_} + {temp-_}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
    temp = int(input())

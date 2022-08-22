import sys

A = int(input())
B = int(input())

x = A * (B%10)
y = A * (B%100 - B%10)
z = A * (B - B%100)

print(x)
print(int(y/10))
print(int(z/100))
print(x+y+z)

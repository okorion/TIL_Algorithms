import sys

input = sys.stdin.readline

word = str(input())
alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for _ in alpha_list:
    if _ in word:
        word = word.replace(_, "0")

print(len(word.strip()))
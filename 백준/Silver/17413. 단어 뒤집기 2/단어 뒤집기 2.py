import sys
input = sys.stdin.readline

word = list(input())

i = 0
start = 0

while i < len(word):
    if word[i] == '<':
        i += 1
        while word[i] != '>':
            i += 1
        i += 1

    elif word[i].isalnum():
        start = i
        while word[i].isalnum() and i < len(word):
            i += 1
        temp = word[start:i]
        temp.reverse()

        word[start:i] = temp

    else:    # 공백
        i += 1


print(''.join(word))

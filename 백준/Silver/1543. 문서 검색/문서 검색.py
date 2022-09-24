import sys

input = sys.stdin.readline

sentence = str(input().strip())
word = str(input().strip())

while word in sentence:
    sentence = sentence.replace(word, "1")

print(sentence.count("1"))

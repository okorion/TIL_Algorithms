import sys

input = sys.stdin.readline

N = int(input())

prime_list = [False] * 2 + [True] * (N - 1)
prime_num = []

for n in range(2, N + 1):
    if prime_list[n]:
        prime_num.append(n)
        for p in range(2 * n, N + 1, n):
            prime_list[p] = False

# print(prime_list)
# print(prime_num)

answer = 0
start = 0
end = 0

while end <= len(prime_num) + 1:
    if sum(prime_num[start:end + 1]) == N:
        # print(start, end, prime_num[start:end + 1])
        answer += 1
        start += 1
    elif sum(prime_num[start:end + 1]) < N:
        end += 1
    elif sum(prime_num[start:end + 1]) > N:
        start += 1

print(answer)

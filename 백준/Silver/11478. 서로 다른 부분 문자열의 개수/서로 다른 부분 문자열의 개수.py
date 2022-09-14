N = str(input())
temp_list = []

for _ in range(1, len(N)+1):
    for n in range(len(N)-_+1):
        temp_list.append(N[n:n+_])

print(len(set(temp_list)))

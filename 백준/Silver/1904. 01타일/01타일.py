import sys
input = sys.stdin.readline

temp = int(input())

if temp > 1:
    N_matrix = [0] * (temp + 1)
    
    N_matrix[1] = 1
    N_matrix[2] = 2
    
    for _ in range(3, temp + 1):
        N_matrix[_] = (N_matrix[_-1] + N_matrix[_-2]) % 15746
    
    print(N_matrix[temp])

else:
    print(1)
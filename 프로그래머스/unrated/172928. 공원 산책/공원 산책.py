def solution(park, routes):
    col_length = len(park[0])
    row_length = len(park)
    start = []
    
    matrix = [[0] * (col_length + 1) for _ in range(row_length + 1)]
    
    for row in range(row_length):
        for col in range(col_length):
            if park[row][col] == 'S':  # 이동 가능한 통로 S일 때는 matrix는 1
                matrix[row][col] = 1
                start.append(row)
                start.append(col)
                
            elif park[row][col] == 'X':  # 이동 가능한 통로 X일 때는 matrix는 2
                matrix[row][col] = 2
                
            else:  # 이동 가능한 통로 O일 때는 matrix는 0
                matrix[row][col] = 0
    
    print(matrix)
    # print(start)    
    
    for route in routes:
        direct, dist = route.split()
        
        if direct == 'E':
            flag = True
            cnt = 1
            
            if start[1] + int(dist) >= col_length:
                flag = False
            else:
                while cnt <= int(dist):
                    if matrix[start[0]][start[1] + cnt] == 0:
                        cnt += 1

                    else:
                        flag = False
                        break

                if flag:
                    matrix[start[0]][start[1]] = 0
                    start[1] += cnt - 1
                
        elif direct == 'W':
            flag = True
            cnt = 1
            
            while cnt <= int(dist):
                if start[1] - cnt >= 0 and matrix[start[0]][start[1] - cnt] == 0:
                    cnt += 1

                else:
                    flag = False
                    break

            if flag:
                matrix[start[0]][start[1]] = 0
                start[1] -= cnt - 1
                
        elif direct == 'S':
            flag = True
            cnt = 1
            
            if start[0] + int(dist) >= row_length:
                flag = False
            else:
                while cnt <= int(dist):
                    if matrix[start[0] + cnt][start[1]] == 0:
                        cnt += 1

                    else:
                        flag = False
                        break

                if flag:
                    matrix[start[0]][start[1]] = 0
                    start[0] += cnt - 1
                
        elif direct == 'N':
            flag = True
            cnt = 1
            
            while cnt <= int(dist):
                if start[0] - cnt >= 0 and matrix[start[0] - cnt][start[1]] == 0:
                    cnt += 1

                else:
                    flag = False
                    break

            if flag:
                matrix[start[0]][start[1]] = 0
                start[0] -= cnt - 1
            
        print(start, flag)
    return start

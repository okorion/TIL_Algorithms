def solution(array, commands):
    answer = []
    
    for start, end, idx in commands:
        # print(array, start, end, array[start - 1:end])
        if end <= len(array):
            answer.append(sorted(array[start - 1:end])[idx - 1])
        else:
            answer.append(sorted(array[start - 1:-1])[idx - 1])
    
    return answer
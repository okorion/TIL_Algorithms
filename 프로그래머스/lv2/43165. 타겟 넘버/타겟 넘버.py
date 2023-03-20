def solution(numbers, target):
    def dfs(count, hap):
        if count == len(numbers):
            # print(hap == 0)
            return (hap == 0)
        
        return dfs(count + 1, hap - numbers[count]) + dfs(count + 1, hap + numbers[count])

    return dfs(0, target)

def solution(prices):
    answer = [0] * len(prices)
    
    for idx, price in enumerate(prices):
        for _ in range(idx+1, len(prices)):
            if prices[_] >= price:
                answer[idx] += 1
            else:
                answer[idx] += 1
                break
                
    return answer
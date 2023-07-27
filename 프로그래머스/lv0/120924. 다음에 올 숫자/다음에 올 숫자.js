function solution(common) {
    const lastElement = common[common.length - 1];
    
    // 등차수열인 경우
    if (common[1] - common[0] === common[common.length - 1] - common[common.length - 2]) {
        const difference = common[1] - common[0];
        return lastElement + difference;
    }
    
    // 등비수열인 경우
    if (common[1] / common[0] === common[common.length - 1] / common[common.length - 2]) {
        const ratio = common[1] / common[0];
        return lastElement * ratio;
    }
    
    // 등차수열과 등비수열이 아닌 경우 (에러 처리)
    return null;
}

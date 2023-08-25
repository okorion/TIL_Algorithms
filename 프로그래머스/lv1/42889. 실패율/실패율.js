function solution(N, stages) {
    const answer = [];
    const stageFailureRates = [];

    for (let i = 1; i <= N; i++) {
        const playersReachedStage = stages.filter(stage => stage >= i).length;
        const playersFailedStage = stages.filter(stage => stage === i).length;
        const failureRate = playersReachedStage === 0 ? 0 : playersFailedStage / playersReachedStage;
        stageFailureRates.push({ stage: i, failureRate: failureRate });
    }

    stageFailureRates.sort((a, b) => {
        if (a.failureRate === b.failureRate) {
            return a.stage - b.stage; // 실패율이 같으면 작은 스테이지 번호 먼저
        }
        return b.failureRate - a.failureRate; // 실패율이 큰 순서대로 정렬
    });

    for (const stageInfo of stageFailureRates) {
        answer.push(stageInfo.stage);
    }

    return answer;
}

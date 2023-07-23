function solution(chicken) {
    let answer = 0;  // 총 서비스 치킨 수를 저장할 변수 초기화
    let couponNum = 0;  // 현재 남은 쿠폰 수를 저장할 변수 초기화

    while (chicken > 0) {
        const totalCoupons = chicken + couponNum;  // 현재 남은 치킨과 이전 주문으로 얻은 쿠폰의 합을 계산
        const serviceChicken = Math.floor(totalCoupons / 10);  // 얻은 쿠폰으로 주문 가능한 서비스 치킨 수 계산

        couponNum = totalCoupons % 10;  // 10장의 쿠폰으로 바꾸지 못한 쿠폰의 수를 저장
        chicken = serviceChicken;  // 서비스 치킨으로 주문한 수를 업데이트

        answer += chicken;  // 주문한 서비스 치킨을 총 서비스 치킨 수에 더함
    }

    return answer;  // 최종 서비스 치킨 수를 반환
}

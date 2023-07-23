function solution(id_pw, db) {
    return db.some(i => i[0] === id_pw[0] && i[1] === id_pw[1]) ? "login" : db.every(i => i[0] !== id_pw[0]) ?  "fail" : "wrong pw";
}
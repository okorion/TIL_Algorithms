function solution(players, m, k) {
    let current_server = []
    let count_server_on = 0
    
    players.forEach((player) => {
        current_server = current_server.map((c) => c - 1).filter((f) => f !== 0)
        
        if (player >= current_server.length * m) {
            const len = current_server.length
            
            for (let i = 0; i < Math.floor(player/m) -  len; i++) {
                current_server.push(k)
                count_server_on += 1
            }
        }
    })
    
    return count_server_on
}
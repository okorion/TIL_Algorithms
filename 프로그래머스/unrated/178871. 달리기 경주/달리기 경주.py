def solution(players, callings):
    rank_dict = {}
    player_dict = {}
    
    for idx, player in enumerate(players):
        player_dict[player] = idx
        rank_dict[idx] = player
        
    for calling in callings:
        cur_rank = player_dict[calling]
        front_rank = cur_rank - 1
        front_player = rank_dict[front_rank]
        
        rank_dict[front_rank], rank_dict[cur_rank] = rank_dict[cur_rank], rank_dict[front_rank]
        player_dict[calling], player_dict[front_player] = player_dict[front_player], player_dict[calling]
        
    return list(rank_dict.values())
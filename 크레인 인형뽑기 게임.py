def solution(board, moves):
    answer = 0
    box = []

    for i in range(len(moves)) : 
        moves[i] -= 1

    for move in moves :
        for i in range(len(board)) : 
            if board[i][move] != 0 : 
                box.append(board[i][move]) 
                board[i][move] = 0 
                break
        if len(box) > 1 : 
            if box[-1] == box[-2] : 
                del box[-1] 
                del box[-1]
                answer += 2 
    return answer


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4] 

#0은 빈 칸을 말하고, 나머지 숫자들은 인형을 뜻한다.

#----------------------------

def solution(board, moves):
    answer = 0
    box = []

    for i in range(len(moves)) : #board 인덱스에 접근하기 때문에, 각 리스트 값에 -1을 해준다.
        moves[i] -= 1

    # moves = [0, 4, 2, 4, 0, 1, 0, 3] - 위의 for문으로 나온 moves

    for move in moves : #moves의 값 들을 board의 열 값으로 준다.
        for i in range(len(board)) : #board의 len값을 board의 행 값으로 준다.
            if board[i][move] != 0 : #crane이 내려가면서, 0이 아닌 값을 만나면 
                box.append(board[i][move]) #다른 바구니에 옮겨 담는다.
                board[i][move] = 0 #그리고 해당 칸은 빈 칸이 된다.
                break
        if len(box) > 1 : #두 개의 인형은 만나면 터트려지므로 길이가 2가 되면
            if box[-1] == box[-2] : #뒤에 담겨진 인형 두개가 만나면
                del box[-1] # [-1] 위치한 인형 두개를 터트린다.
                del box[-1]
                answer += 2 # 인형 두 개가 터졌으므로, result값에 2를 더한다.
    return answer


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(lottos, win_nums):
    answer = []
    lotto_rank = {
        6 : 1, 
        5 : 2,
        4 : 3, 
        3 : 4,
        2 : 5,
        1 : 6,
        0 : 6
    }
    worst_cnt = 0
    for first_idx in range(len(lottos)) :
        if lottos[first_idx] in win_nums :
            worst_cnt += 1
    answer.append(lotto_rank[worst_cnt])
    
    for i in range(len(lottos)) :
        for j in range(len(win_nums)) :
            if lottos[i] == win_nums[j] :
                lottos.insert(j, lottos.pop(i))
            
    best_cnt = 0
    for second_idx in range(len(lottos)) :
        if lottos[second_idx] == 0 :
            lottos[second_idx] = win_nums[second_idx]
        if lottos[second_idx] in win_nums :
            best_cnt += 1
    answer.append(lotto_rank[best_cnt])
    return sorted(answer)


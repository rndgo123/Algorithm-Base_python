#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(answers):
    answer = []

    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    one = one[:len(answers)]
    two = two[:len(answers)]
    three = three[:len(answers)]

    one_cnt = 0
    two_cnt = 0
    three_cnt = 0

    for i in range(len(answers)) :
        if answers[i] == one[i] :
            one_cnt += 1
        if answers[i] == two[i] :
            two_cnt += 1    
        if answers[i] == three[i] :
            three_cnt += 1

    rank = [one_cnt, two_cnt, three_cnt]

    for j in range(len(rank)) :
        if rank[j] >= max(rank) :
            answer.append(j+1)

    return answer


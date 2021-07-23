#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input())
player = [tuple(map(int, input().split())) for _ in range(n)]

player.sort(reverse=True)

max_weight = 0
cnt = 0

for length, weight in player :
    if weight > max_weight:
        max_weight = weight
        cnt += 1
        
print(cnt)


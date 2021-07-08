#!/usr/bin/env python
# coding: utf-8

# In[39]:


#봉우리 - 내 코드

n = int(input())
peak = [list(map(int, input())) for _ in range(n)]
peak.insert(0, [0]*n)
peak.append([0]*n)
for p in peak :
    p.insert(0,0)
    p.append(0)

result = 0

#-----------code---------------------#
for i in range(1, len(peak)-1) : #row
    for j in range(1, len(peak)-1) : #col
        if peak[i][j] > peak[i][j-1] and peak[i][j] > peak[i-1][j] and peak[i][j] > peak[i+1][j] and peak[i][j] > peak[i][j+1] :
            result += 1
print(result)
            


# In[43]:


#봉우리 - 풀이
#상하좌우 탐색문제는 dx, dy리스트로 해결한다
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
peak = [list(map(int, input().split())) for _ in range(n)]
peak.insert(0, [0]*n)
peak.append([0]*n)
for p in peak :
    p.insert(0,0)
    p.append(0)

result = 0

#-----------code---------------------#
for i in range(1, n+1) : #row
    for j in range(1, n+1) : #col
        if all(peak[i][j] > peak[i+dx[k]][j+dy[k]] for k in range(4)) :
            result += 1
        
print(result)


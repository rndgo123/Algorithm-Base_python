#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#이분탐색 - 랜선 자르기

n, result = map(int, input().split())
num = []

for j in range(n) :
    lan = int(input())
    num.append(lan)

end = max(num)
start = 0

while start <= end :
    mid = (start + end) // 2
    cnt = 0
    for i in num :
        cnt += (i // mid)
    if cnt >= result :
        start = mid + 1
    else :
        end = mid - 1

print(mid)


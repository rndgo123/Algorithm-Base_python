n, c = map(int, input().split())

stable = [int(input()) for _ in range(n)]
stable.sort()

def _count(mid) :
    location = min(stable)
    cnt = 1
    for i in stable :
        if (i - location) >= mid :
            location = i
            cnt += 1
    return cnt
            
left = min(stable)
right = max(stable)

result = 0

while left <= right :
    mid = (left + right) // 2
    if _count(mid) >= c :
        result = mid
        left = mid + 1
    else :
        right = mid - 1
        
print(result)


#나의 풀이 - 오답
n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]

test = int(input())

for _ in range(test) :
    row, direction, num = map(int, input().split())
    if direction == 0 :
        left = tree[row-1][:num]
        right = tree[row-1][num:]
        right.extend(left)
        tree[row-1] = right
    else : 
        left = tree[row-1][:-num]
        right = tree[row-1][-num:]
        right.extend(left)
        tree[row-1] = right
        
result = 0
s = 0
e = n - 1

for i in range(n) :
    for j in range(s, e+1) :
        result += tree[i][j]
    if i < n//2 :
        s += 1
        e -= 1
    else :
        s -= 1
        e += 1
        
print(result)

#풀이

n = 5
tree = [list(map(int, input().split())) for _ in range(n)]

test = 3

for i in range(test) :
    row, direction, num = map(int, input().split())
    if direction == 0 :
        for _ in range(num) :
            tree[row-1].append(tree[row-1].pop(0))
    else :
        for _ in range(num) :
            tree[row-1].insert(0, tree[row-1].pop())
result = 0
start = 0
end = n - 1

for i in range(n) :
    for j in range(start, end+1) :
        result += tree[i][j]
    if i < n//2 :
        start += 1
        end -= 1
    else :
        start -= 1
        end += 1
        
print(result)


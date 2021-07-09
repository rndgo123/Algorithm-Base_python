#내 코드
grid = [list(map(int, input().split())) for _ in range(9)]

dx = [-1,-1,-1,0,0,0,1,1,1]
dy = [-1,0,1,-1,0,1,-1,0,1]

_bool = True

for i in range(1, len(grid), 3) :
    for j in range(1, len(grid), 3) :
        _list = [0] * 9
        for k in range(9) :
            _list[(grid[i+dx[k]][j+dy[k]]) - 1] += 1
        for num in _list :
            if num != 1 :
                _bool = False
    

        
if _bool == True :
    print('YES')
else :
    print('NO')



#풀이 코드
grid = [list(map(int, input().split())) for _ in range(9)]

def check(grid) :
    for i in range(9) :
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9) :
            ch1[grid[i][j]] = 1
            ch2[grid[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9 :
            return False
    for i in range(3) :
        for j in range(3) :
            ch3 = [0]*10
            for k in range(3) :
                for s in range(3) :
                    ch3[grid[i*3 + k][j*3 + s]] = 1
            if sum(ch3) != 9 :
                return False
    return True

if check(grid) :
    print('YES')
else :
    print('NO')


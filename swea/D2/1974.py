T = int(input())

def check_first():
    for i in range(9):
        cnt = [0]*9
        for j in range(9):
            if cnt[board[i][j]-1]==0:
                cnt[board[i][j]-1]=1
            else:
                return 0
    return 1

def check_second():
    for j in range(9):
        cnt = [0]*9
        for i in range(9):
            if cnt[board[i][j]-1]==0:
                cnt[board[i][j]-1]=1
            else:
                return 0
    return 1

def check_third():
    for n in range(3):
        for m in range(3):
            cnt = [0]*9
            for x in range(3):
                i = n*3+x
                for y in range(3):
                    j=m*3+y
                    if cnt[board[i][j]-1]==0:
                        cnt[board[i][j]-1]=1
                    else:
                        return 0
    return 1

for t in range(T):
    board = [list(map(int, input().split())) for _ in range(9)]
    flag=0

    if check_first()==0:
        print('#%d %d' % (t+1, 0))
        continue

    if check_second()==0:
        print('#%d %d' % (t+1, 0))
        continue

    if check_third()==0:
        print('#%d %d' % (t+1, 0))
        continue

    print('#%d %d' % (t+1, 1))
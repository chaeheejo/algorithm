board = []
for _ in range(4):
    n1,d1,n2,d2,n3,d3,n4,d4 = map(int, input().split())
    board.append([[n1,d1-1],[n2,d2-1],[n3,d3-1],[n4,d4-1]])

def find_loc(tboard,n):
    for i in range(4):
        for j in range(4):
            if tboard[i][j][0]==n:
                return i,j
    return -1,-1

dxy = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
def move_thief(tboard, ti, tj):
    for n in range(16):
        i,j = find_loc(tboard,n+1)
        if i==-1:
            continue
        d = tboard[i][j][1]
        for k in range(8):
            nx,ny = i+dxy[(d+k)%8][0],j+dxy[(d+k)%8][1]
            if 0<=nx<4 and 0<=ny<4:
                if nx==ti and ny==tj:
                    continue
                tboard[nx][ny], tboard[i][j]= tboard[i][j], tboard[nx][ny]
                tboard[nx][ny][1] = (d+k)%8
                break

def duplicate_board(tboard):
    new_board = [[[0,0] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_board[i][j][0] = tboard[i][j][0]
            new_board[i][j][1] = tboard[i][j][1]
    return new_board

def move_tag():
    answer=0
    queue=[[[b[:] for b in board],0,0,board[0][0][1],board[0][0][0]]]
    queue[0][0][0][0] = [0,0]
    cur=0
    while cur<len(queue):
        cur_board,i,j,d,score=queue[cur]
        if score>=answer:
            answer=score
        cur+=1
        move_thief(cur_board,i,j)
        nx,ny = i,j
        for _ in range(3):
            nx,ny = nx+dxy[d][0],ny+dxy[d][1]
            if 0<=nx<4 and 0<=ny<4 and cur_board[nx][ny][0]>0:
                cv,cd = cur_board[nx][ny]
                cur_board[nx][ny] = [0,0]
                tmp_board = duplicate_board(cur_board)
                queue.append([tmp_board,nx,ny,cd,score+cv])
                cur_board[nx][ny] = [cv,cd]
    return answer
    
print(move_tag())
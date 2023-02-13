N, M, K = map(int, input().split())
board = [[[0]]*N for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        board[i][j] = [tmp[j]]

point=[0]*M
player_xy, player_info = [], []
for _ in range(M):
    x,y,d,s = map(int, input().split())
    player_xy.append([x-1,y-1])
    player_info.append([d,s,0])

def switch_gun(bx,by,pi):
    max_gun = max(board[bx][by])
    if max_gun>player_info[pi][2]:
        gi = board[bx][by].index(max_gun)
        board[bx][by][gi] = player_info[pi][2]
        player_info[pi][2] = max_gun

dxy = [(-1,0),(0,1),(1,0),(0,-1)]
for _ in range(K):
    for i in range(M):
        x,y = player_xy[i]
        d,s,g = player_info[i]

        nx,ny = x+dxy[d][0], y+dxy[d][1]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            d = (d+2)%4
            nx,ny = x+dxy[d][0], y+dxy[d][1]
            player_info[i][0] = d

        if [nx,ny] not in player_xy:
            if board[nx][ny]:
                switch_gun(nx,ny,i)
            player_xy[i][0],player_xy[i][1] = nx,ny
        else:
            loser, winner = -1, -1

            ri = player_xy.index([nx,ny])

            rival_value = player_info[ri][1] + player_info[ri][2]
            cur_value = player_info[i][1] + player_info[i][2]

            if cur_value<rival_value:
                loser,winner = i,ri
            elif rival_value<cur_value:
                loser,winner = ri,i
            else:
                if player_info[ri][1]<player_info[i][1]:
                    loser,winner = ri,i
                else:
                    loser,winner = i,ri

            point[winner] += abs(rival_value-cur_value)

            player_xy[i][0], player_xy[i][1] = nx, ny

            if player_info[loser][2]!=0:
                board[nx][ny].append(player_info[loser][2])
                player_info[loser][2] = 0

            for k in range(4):
                ld = (player_info[loser][0]+k)%4
                lx,ly = nx+dxy[ld][0], ny+dxy[ld][1]
                if 0<=lx<N and 0<=ly<N and [lx,ly] not in player_xy:
                    player_xy[loser][0], player_xy[loser][1] = lx,ly
                    player_info[loser][0] = ld
                    if board[lx][ly]:
                        switch_gun(lx,ly,loser)
                    break

            switch_gun(nx,ny,winner)

for p in point:
    print(p, end=' ')
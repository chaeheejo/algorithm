R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]
R-=1
C-=1

def sort_row():
    global board
    new_board = []
    max_row = 0
    for i in range(len(board)):
        dic = {}
        for j in range(len(board[0])):
            if board[i][j]==0:
                continue
            if board[i][j] not in dic:
                dic[board[i][j]]=1
            else:
                dic[board[i][j]]+=1
        sorted_dic = sorted(dic.items(),key=lambda x:(x[1],x[0]))
        new_row = []
        for k in range(len(sorted_dic)):
            if k>=100:
                break
            new_row.extend([sorted_dic[k][0],sorted_dic[k][1]])
        new_board.append(new_row)
        max_row = max(max_row,len(new_row))
    for new in new_board:
        if len(new)<max_row:
            new = new.extend([0]*(max_row-len(new)))
    board = new_board

def sort_col():
    global board
    new_board = []
    max_col = 0
    for j in range(len(board[0])):
        dic = {}
        for i in range(len(board)):
            if board[i][j]==0:
                continue
            if board[i][j] not in dic:
                dic[board[i][j]] = 1
            else:
                dic[board[i][j]] += 1
        sorted_dic = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        new_col = []
        for k in range(len(sorted_dic)):
            if k >= 100:
                break
            new_col.extend([sorted_dic[k][0], sorted_dic[k][1]])
        new_board.append(new_col)
        max_col = max(max_col,len(new_col))
    for new in new_board:
        if len(new)<max_col:
            new = new.extend([0]*(max_col-len(new)))
    new_board = list(zip(*new_board))
    board = new_board

answer=-1
for k in range(100):
    if R<len(board) and C<len(board[R]) and board[R][C]==K:
        answer=k
        break
    if len(board)>=len(board[0]):
        sort_row()
    else:
        sort_col()
print(answer)
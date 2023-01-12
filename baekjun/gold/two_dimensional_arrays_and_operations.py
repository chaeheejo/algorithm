N,M,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

def operate(board,flag):
    new_board, length = [],0
    for row in board:
        new_row, cnt_num = [],[]
        for num in set(row):
            if num==0:
                continue
            cnt_num.append((num,row.count(num)))
        cnt_num = sorted(cnt_num, key=lambda x:[x[1],x[0]])
        for num,cnt in cnt_num:
            new_row+=[num,cnt]
        new_board.append(new_row)
        length = max(length, len(new_row))

    for row in new_board:
        row += [0]*(length-len(row))
        if len(row)>100:
            row = row[:100]

    if flag=='C':
        return list(zip(*new_board))
    else:
        return new_board

answer=-1
for k in range(101):
    if 0<=N-1<len(board) and 0<=M-1<len(board[0]) and board[N-1][M-1]==K:
        answer=k
        break

    if len(board)>=len(board[0]):
        board = operate(board,'R')
    else:
        board = operate(list(zip(*board)),'C')

print(answer)
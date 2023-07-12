T = int(input())

for t in range(T):
    _ = input()
    board = list(map(int, input().split()))
    check = [0]*1000

    for i in range(len(board)):
        check[board[i]-1]+=1

    max_cnt = max(check)
    answer=0
    for i in range(len(board)-1,-1,-1):
        if check[i]==max_cnt:
            answer = i+1
            break

    print('#%d %d' % (t+1, answer))
index = [[1], [2], [3], [4], [5], [6, 21],
         [7], [8], [9], [10], [11, 25],
         [12], [13], [14], [15], [16, 27],
         [17], [18], [19], [20], [32],
         [22], [23], [24], [30], [26],
         [24], [28], [29], [24], [31], [20], [32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
dice = list(map(int, input().split()))

def backtracking(depth, result, horse):
    global answer
    if depth >= 10:
        answer = max(answer, result)
        return
    for i in range(4):
        cur = horse[i]
        if len(index[cur]) == 2:
            cur = index[cur][1]
        else:
            cur = index[cur][0]

        for j in range(dice[depth]-1):
            cur = index[cur][0]

        if cur == 32 or (cur < 32 and cur not in horse):
            before = horse[i]
            horse[i] = cur
            backtracking(depth + 1, result + score[cur], horse)
            horse[i] = before

answer = 0
backtracking(0, 0, [0,0,0,0])
print(answer)
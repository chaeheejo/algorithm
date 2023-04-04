cmd = list(map(int, input().split()))

next_score = [[1],[2],[3],[4],[5],[6,21],
              [7],[8],[9],[10],[11,25],
              [12],[13],[14],[15],[16,27],
              [17],[18],[19],[20],[32],
              [22],[23],[24],[30],[26],
              [24],[28],[29],[24],[31],[20],[32]]
score = [0,2,4,6,8,10,
         12,14,16,18,20,
         22,24,26,28,30,
         32,34,36,38,40,
         13,16,19,25,22,
         24,28,27,26,30,35,0]

def backtracking(depth,result,horse):
    global answer
    if depth>=10:
        answer = max(answer,result)
        return

    for i in range(4):
        cur_idx = horse[i]
        if len(next_score[cur_idx])==2:
            cur_idx = next_score[cur_idx][1]
        else:
            cur_idx = next_score[cur_idx][0]

        for _ in range(cmd[depth]-1):
            cur_idx = next_score[cur_idx][0]

        if cur_idx==32 or (cur_idx<32 and cur_idx not in horse):
            tmp = horse[i]
            horse[i] = cur_idx
            backtracking(depth+1,result+score[cur_idx],horse)
            horse[i] = tmp

answer = 0
backtracking(0,0,[0,0,0,0])
print(answer)
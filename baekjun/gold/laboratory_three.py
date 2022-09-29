N, M = map(int, input().split())
virus_map = [list(input().split()) for _ in range(N)]

virus_location = []
blank_cnt=0
for i in range(N):
    for j in range(N):
        if virus_map[i][j]=='1':
            virus_map[i][j]=-100
        elif virus_map[i][j]=='2':
            virus_location.append((i,j))
            virus_map[i][j]=-200
        elif virus_map[i][j]=='0':
            virus_map[i][j]=-300
            blank_cnt+=1

def combination(arr, num):
    for i in range(len(arr)):
        if num==1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:], num-1):
                yield [arr[i]]+next

chosen_location=[]
for i in combination(range(len(virus_location)) ,M):
    chosen_location.append(i)

def max_cycle(map):
    tmp=[]
    for i in range(N):
        tmp.append(max(map[i]))
    return max(tmp)

answer=[]
for i in range(len(chosen_location)):
    tmp_map=virus_map[:]
    global cnt
    cnt=blank_cnt

    def virus_spread(spread_index):
        global cnt
        if cnt==0:
            return
        i, j = spread_index
        if -1<i-1<N and -1<j<N:
            if tmp_map[i-1][j]==-300:
                tmp_map[i-1][j]=tmp_map[i][j] + 1
                cnt-=1
                virus_spread([i-1,j])
        if -1<i+1<N and -1<j<N:
            if tmp_map[i+1][j]==-300:
                tmp_map[i+1][j]=tmp_map[i][j] + 1
                cnt -= 1
                virus_spread([i+1, j])
        if -1<i<N and -1<j+1<N:
            if tmp_map[i][j+1] == -300:
                tmp_map[i][j+1] = tmp_map[i][j] + 1
                cnt -= 1
                virus_spread([i, j+1])
        if -1<i<N and -1<j-1<N:
            if tmp_map[i][j-1] == -300:
                tmp_map[i][j-1] = tmp_map[i][j] + 1
                cnt -= 1
                virus_spread([i, j-1])


    for index in range(len(virus_location)):
        if index in chosen_location[i]:
            i, j = virus_location[index]
            tmp_map[i][j] = 0
            virus_spread([i, j])

    answer.append(max_cycle(tmp_map))

print(answer)
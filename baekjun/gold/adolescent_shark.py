map_sea=[[[0,0] for _ in range(4)] for _ in range(4)]
for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    map_sea[i][0] = [a1, b1]
    map_sea[i][1] = [a2, b2]
    map_sea[i][2] = [a3, b3]
    map_sea[i][3] = [a4, b4]

direction = {1:(-1,0), 2:(-1,-1), 3:(0,-1), 4:(1,-1), 5:(1,0), 6:(1,1), 7:(0,1), 8:(-1,1)}

def find_fish(temp_map, n):
    for i in range(4):
        for j in range(4):
            if temp_map[i][j][0] == n:
                return i, j
    return -1,-1

def move_fish(temp_map):
    for n in range(1, 17):
        cur_i, cur_j = find_fish(temp_map, n)

        if cur_i==-1:
            continue

        drc = temp_map[cur_i][cur_j][1]

        move_i, move_j, flag = 0, 0, 0
        for _ in range(8):
            move_i = cur_i + direction[drc][0]
            move_j = cur_j + direction[drc][1]
            if 0 <= move_i < 4 and 0 <= move_j < 4 and temp_map[move_i][move_j][0] > -1:
                flag = 1
                break
            else:
                drc = (drc + 1) % 8
                if drc == 0:
                    drc = 8
        if flag:
            temp_map[cur_i][cur_j][1] = drc
            tmp_fish = temp_map[cur_i][cur_j]
            temp_map[cur_i][cur_j] = temp_map[move_i][move_j]
            temp_map[move_i][move_j] = tmp_fish

    return temp_map

def copy_item(temp_map):
    new_map = [[[0,0] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(2):
                new_map[i][j][k] = temp_map[i][j][k]
    return new_map

def move_shark(temp_map, i, j):
    total=[]

    cur_index, queue = 0, [[temp_map, i, j, 0]]
    while cur_index<len(queue):
        cur_map, tmp_i, tmp_j, cnt = queue[cur_index]
        cur_map = copy_item(cur_map)

        shark_drc = cur_map[tmp_i][tmp_j][1]
        cnt += cur_map[tmp_i][tmp_j][0]
        total.append(cnt)
        cur_map[tmp_i][tmp_j][0] = -1
        cur_index+=1

        cur_map = move_fish(cur_map)

        cur_map[tmp_i][tmp_j] = [0,0]

        shark_i, shark_j = tmp_i, tmp_j
        for _ in range(4):
            shark_i += direction[shark_drc][0]
            shark_j += direction[shark_drc][1]
            if 0<=shark_i<4 and 0<=shark_j<4 and cur_map[shark_i][shark_j][0]>0:
                queue.append([cur_map, shark_i, shark_j, cnt])

    return max(total)

print(move_shark(map_sea, 0, 0))
N = int(input())

map = []
for _ in range(N):
    map.append(list(input().split(' ')))

obstacle = []
teacher = []
for i in range(N):
    for j in range(N):
        if map[i][j] == 'T':
            teacher.append((i, j))
        elif map[i][j] == 'X':
            obstacle.append((i, j))

move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def check_surveillance(map):
    for x, y in teacher:
        for i in range(4):
            tmpx = x
            tmpy = y
            while 0 <= tmpx + move[i][0] < N and 0 <= tmpy + move[i][1] < N:
                tmpx += move[i][0]
                tmpy += move[i][1]

                if map[tmpx][tmpy] == 'O':
                    break
                elif map[tmpx][tmpy] == 'S':
                    return False
    return True

def set_obstacle():
    for i in range(len(obstacle)):
        xi, yi = obstacle[i]
        map[xi][yi] = 'O'
        for j in range(i + 1, len(obstacle)):
            xj, yj = obstacle[j]
            map[xj][yj] = 'O'
            for k in range(j + 1, len(obstacle)):
                xk, yk = obstacle[k]
                map[xk][yk] = 'O'

                if check_surveillance(map):
                    return True

                map[xk][yk] = 'X'
            map[xj][yj] = 'X'
        map[xi][yi] = 'X'

    return False

answer = set_obstacle()
if answer:
    print('YES')
else:
    print('NO')

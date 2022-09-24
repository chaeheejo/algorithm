A, B = map(int,input().split())
N, M = map(int,input().split())

map = [['X']*A for _ in range(B)]
go = {'N':(-1,0), 'W':(0,-1), 'S':(1,0), 'E':(0,1)}
left = ['N', 'W', 'S', 'E']
right = ['E', 'S', 'W', 'N']

robot=[]
for i in range(N):
    x, y, dir = input().split()
    x = int(x)-1
    y = B-int(y)
    map[y][x] = str(i+1)
    robot.append([y,x,dir])

def simulate():
    answer = ''
    for _ in range(M):
        i, order, repeat = input().split()
        i = int(i) -1
        repeat = int(repeat)
        x, y, cur_dir = robot[i]

        if order=='F':
            tmpx = x
            tmpy = y
            for _ in range(repeat):
                tmpx += go[cur_dir][0]
                tmpy += go[cur_dir][1]

                if answer=='':
                    if 0>tmpx or tmpx>=B or 0>tmpy or tmpy>=A:
                            answer = 'Robot '+str(i+1)+' crashes into the wall'
                    elif map[tmpx][tmpy]!='X':
                        answer = 'Robot '+str(i+1)+' crashes into robot '+map[tmpx][tmpy]
                    else:
                        map[tmpx-go[cur_dir][0]][tmpy-go[cur_dir][1]]='X'
                        map[tmpx][tmpy]=str(i+1)
                        robot[i] = [tmpx, tmpy, cur_dir]
        else:
            if order=='L':
                dir_index = left.index(cur_dir)
                dir_index += repeat
                robot[i] = [x, y, left[dir_index % 4]]
            elif order=='R':
                dir_index = right.index(cur_dir)
                dir_index += repeat
                robot[i] = [x, y, right[dir_index % 4]]
    if answer=='':
        answer='OK'
    return answer

print(simulate())

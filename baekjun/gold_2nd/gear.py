gear = [list(map(int, input())) for _ in range(4)]
K = int(input())
move = [list(map(int, input().split())) for _ in range(K)]

for g,d in move:
    g-=1
    move_neighbor=[(g,d)]
    left_g, right_g, tmp = g,g,d
    while left_g>0:
        if gear[left_g][6]!=gear[left_g-1][2]:
            tmp *= (-1)
            left_g-=1
            move_neighbor.append((left_g, tmp))
        else:
            break
    tmp = d
    while right_g<3:
        if gear[right_g][2]!=gear[right_g+1][6]:
            tmp *= (-1)
            right_g+=1
            move_neighbor.append((right_g, tmp))
        else:
            break

    for n,r in move_neighbor:
        if r==1:
            gear[n] = [gear[n][i - 1] for i in range(8)]
        else:
            gear[n] = [gear[n][i + 1] if i < 7 else gear[n][0] for i in range(8)]

answer=0
for i in range(4):
    if gear[i][0]==1:
        answer+=(2**i)
print(answer)
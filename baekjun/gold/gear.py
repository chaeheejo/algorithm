gear = list()

for i in range(4):
    tmp = list(input())
    gear.append(tmp)

num = int(input())

method = []
for _ in range(num):
    tmp = list(map(int, input().split()))
    method.append(tmp)


def rotate(gear, side):
    if side:
        return [gear[i - 1] for i in range(8)]
    else:
        return [gear[i + 1] if i < 7 else gear[0] for i in range(8)]


visited = []
def move_gear(change_gear_num, side):
    visited.append(change_gear_num)

    if 0 <= change_gear_num - 1:
        if gear[change_gear_num][6] != gear[change_gear_num - 1][2] and change_gear_num-1 not in visited:
            move_gear(change_gear_num - 1, not side)
    if change_gear_num+1 <=3:
        if gear[change_gear_num][2] != gear[change_gear_num+1][6] and change_gear_num+1 not in visited:
            move_gear(change_gear_num+1, not side)

    gear[change_gear_num] = rotate(gear[change_gear_num], side)


for i in range(num):
    change_gear_num = method[i][0] - 1

    if method[i][1] == 1:
        side = True
    else:
        side = False

    visited.clear()
    move_gear(change_gear_num, side)

answer=0
if gear[0][0]=='1':
    answer+=1
if gear[1][0]=='1':
    answer+=2
if gear[2][0]=='1':
    answer+=4
if gear[3][0]=='1':
    answer+=8

print(answer)
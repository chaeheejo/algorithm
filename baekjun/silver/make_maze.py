N = int(input())
command = input()

my_direction = 100
my_location = [[0, 0]]
curr_location = [0, 0]
for i in range(N):
    if command[i] == 'L':
        my_direction -= 1
    elif command[i] == 'R':
        my_direction += 1

    elif command[i] == 'F':
        if my_direction % 4 == 0:
            curr_location[0] += 1
        elif my_direction % 4 == 1:
            curr_location[1] -= 1
        elif my_direction % 4 == 2:
            curr_location[0] -= 1
        elif my_direction % 4 == 3:
            curr_location[1] += 1
        my_location.append(curr_location[:])

min_i, min_j, max_i, max_j = 100, 100, 0, 0
for i, j in my_location:
    if min_i > i:
        min_i = i
    if max_i < i:
        max_i = i
    if min_j > j:
        min_j = j
    if max_j < j:
        max_j = j

answer = [['#'] * (abs(max_j - min_j) + 1) for _ in range(abs(max_i - min_i) + 1)]

if min_i != 0:
    for i in range(len(my_location)):
        my_location[i][0] += min_i * (-1)
if min_j != 0:
    for i in range(len(my_location)):
        my_location[i][1] += min_j * (-1)

for i, j in my_location:
    answer[i][j] = '.'

for ans in answer:
    for a in ans:
        print(a, end='')
    print()
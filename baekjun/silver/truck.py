from collections import deque

T, NUM, MAX = map(int, input().split(' '))
truck = list(map(int,input().split(' ')))

bridge = deque(list([0 for _ in range(NUM)]))

answer=0
cur_truck=0
total_weight=0
while True:
    last_weight = bridge.popleft()
    total_weight-=last_weight

    if cur_truck==T:
        answer+=NUM
        break

    if (total_weight+truck[cur_truck]) <= MAX:
        bridge.append(truck[cur_truck])
        total_weight+=truck[cur_truck]
        cur_truck+=1
        answer+=1
    else:
        bridge.append(0)
        answer+=1

print(answer)
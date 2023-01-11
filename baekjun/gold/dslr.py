T = int(input())
cmd = [list(map(int, input().split())) for _ in range(T)]

for t in range(T):
    start, end = cmd[t][0], cmd[t][1]
    way = [''] * 10000
    way[start]=' '

    answer=[]
    queue=[start]
    cur=0
    while cur<len(queue):
        num = queue[cur]
        cur+=1

        if num==end:
            break

        tmp = num*2
        tmp = tmp % 10000
        if way[tmp]== '':
            way[tmp]= way[num] + 'D'
            queue.append(tmp)

        tmp = num-1
        if num==0:
            tmp=9999
        if way[tmp]== '':
            way[tmp]= way[num] + 'S'
            queue.append(tmp)

        tmp = (num%1000)*10 + num // 1000
        if way[tmp]== '':
            way[tmp]= way[num] + 'L'
            queue.append(tmp)

        tmp = (num%10)*1000 + num//10
        if way[tmp] == '':
            way[tmp] = way[num] + 'R'
            queue.append(tmp)

    print(way[end])
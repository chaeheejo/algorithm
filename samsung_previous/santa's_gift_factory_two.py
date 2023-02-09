N = int(input())
command = [list(map(int, input().split())) for _ in range(N)]
head,tail,nxt,prv,num_item = [],[],[],[],[]

def create(cmd):
    global head,tail,nxt,prv,num_item
    head,tail,num_item = [0]*(cmd[1]+1),[0]*(cmd[1]+1),[0]*(cmd[1]+1)
    nxt,prv = [0]*(cmd[2]+1),[0]*(cmd[2]+1)

    for item in range(1,cmd[2]+1):
        belt = cmd[item+2]
        if num_item[belt]==0:
            head[belt],tail[belt]=item,item
            num_item[belt]+=1
        else:
            original_tail = tail[belt]
            nxt[original_tail]=item
            prv[item] = original_tail
            tail[belt] = item
            num_item[belt]+=1

def move_all(cmd):
    src,dst = cmd[1],cmd[2]
    if num_item[src]==0:
        print(num_item[dst])
        return

    if num_item[dst]==0:
        head[dst] = head[src]
        tail[dst] = tail[src]
    else:
        dst_head = head[dst]
        src_tail = tail[src]
        head[dst] = head[src]
        nxt[src_tail] = dst_head
        prv[dst_head] = src_tail

    head[src], tail[src] = 0,0

    num_item[dst] += num_item[src]
    num_item[src]=0

    print(num_item[dst])

def remove_head(belt):
    if num_item[belt]==0:
        return 0

    if num_item[belt]==1:
        belt_head = head[belt]
        head[belt],tail[belt] = 0,0
        num_item[belt]=0
        return belt_head

    belt_head = head[belt]
    head_next = nxt[belt_head]
    nxt[belt_head], prv[head_next] = 0,0
    num_item[belt] -= 1
    head[belt] = head_next

    return belt_head

def push_head(belt,item):
    if item==0:
        return

    if num_item[belt]==0:
        head[belt], tail[belt] = item,item
        num_item[belt]=1
    else:
        belt_head = head[belt]
        head[belt] = item
        nxt[item] = belt_head
        prv[belt_head] = item
        num_item[belt]+=1

def change_head(cmd):
    src,dst = cmd[1],cmd[2]

    src_head = remove_head(src)
    dst_head = remove_head(dst)
    push_head(dst,src_head)
    push_head(src,dst_head)

    print(num_item[dst])

def divide(cmd):
    src,dst = cmd[1],cmd[2]

    cnt = num_item[src]
    tmp=[]
    for _ in range(cnt//2):
        tmp.append(remove_head(src))

    for i in range(len(tmp)-1,-1,-1):
        push_head(dst,tmp[i])

    print(num_item[dst])

def get_item_score(cmd):
    item = cmd[1]

    a,b=0,0
    if prv[item]!=0:
        a = prv[item]
    else:
        a = -1

    if nxt[item]!=0:
        b = nxt[item]
    else:
        b = -1

    print(a+2*b)

def get_belt_score(cmd):
    belt = cmd[1]

    a,b,c=0,0,num_item[belt]
    if head[belt]!=0:
        a = head[belt]
    else:
        a = -1

    if tail[belt]!=0:
        b = tail[belt]
    else:
        b = -1

    print(a+2*b+3*c)

for i in range(N):
    if command[i][0]==100:
        create(command[i])
    elif command[i][0]==200:
        move_all(command[i])
    elif command[i][0]==300:
        change_head(command[i])
    elif command[i][0]==400:
        divide(command[i])
    elif command[i][0]==500:
        get_item_score(command[i])
    else:
        get_belt_score(command[i])
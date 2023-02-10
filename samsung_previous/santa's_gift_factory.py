from collections import defaultdict

N, M = -1,-1
prv,nxt = defaultdict(lambda :0), defaultdict(lambda :0)
head, tail = [0]*10, [0]*10
weight={}
belt_num = defaultdict(lambda :-1)
broken = [False]*10

def create(cmd):
    global N,M

    N, M = cmd[1], cmd[2]
    ids, ws = cmd[3:3+N],cmd[3+N:3+2*N]

    for i in range(N):
        weight[ids[i]] = ws[i]

    size = N//M
    for i in range(M):
        next_size = (i+1)*size
        head[i] = ids[i*size]
        tail[i] = ids[next_size-1]
        for j in range(i*size,next_size):
            belt_num[ids[j]] = i
            if j<next_size-1:
                nxt[ids[j]] = ids[j+1]
                prv[ids[j+1]] = ids[j]

def remove_id(id,flag):
    belt = belt_num[id]

    if flag:
        belt_num[id]=-1

    if head[belt] == tail[belt]:
        head[belt], tail[belt] = 0,0
    elif id == head[belt]:
        nid = nxt[id]
        head[belt] = nid
        prv[nid] = 0
    elif id == tail[belt]:
        pid = prv[id]
        tail[belt] = pid
        nxt[pid] = 0
    else:
        pid,nid = prv[id], nxt[id]
        nxt[pid] = nid
        prv[nid] = pid
    nxt[id], prv[id] = 0,0

def push_id(pid,id):
    nxt[pid] = id
    prv[id] = pid

    belt = belt_num[pid]
    if tail[belt] == pid:
        tail[belt] = id

def pop(cmd):
    max_w = cmd[1]

    rtn=0
    for belt in range(M):
        if broken[belt]:
            continue
        if head[belt]!=0:
            id = head[belt]
            w = weight[id]
            if w<=max_w:
                rtn+=w
                remove_id(id,True)
            elif nxt[id]!=0:
                remove_id(id,False)
                push_id(tail[belt],id)
    print(rtn)

def remove(cmd):
    id = cmd[1]

    if belt_num[id] == -1:
        print(-1)
        return

    remove_id(id,True)
    print(id)

def check(cmd):
    id = cmd[1]

    if belt_num[id] == -1:
        print(-1)
        return

    belt = belt_num[id]
    if head[belt] != id:
        original_tail,original_head = tail[belt],head[belt]
        new_tail = prv[id]
        tail[belt] = new_tail
        head[belt] = id

        nxt[original_tail] = original_head
        prv[original_head] = original_tail
        prv[id] = 0
        nxt[new_tail] = 0
    print(belt+1)

def broken_belt(cmd):
    belt = cmd[1]
    belt -= 1

    if broken[belt]:
        print(-1)
        return

    broken[belt] = True

    if head[belt]==0:
        print(belt+1)
        return

    nxt_belt = belt
    while True:
        nxt_belt = (nxt_belt+1)%M
        if not broken[nxt_belt]:
            if tail[nxt_belt]==0:
                head[nxt_belt] = head[belt]
                tail[nxt_belt] = tail[belt]
            else:
                push_id(tail[nxt_belt],head[belt])
                tail[nxt_belt] = tail[belt]

            id = head[belt]
            while id!=0:
                belt_num[id] = nxt_belt
                id = nxt[id]

            head[belt], tail[belt] = 0,0
            break
    print(belt+1)

K = int(input())
for _ in range(K):
    cmd = list(map(int, input().split()))
    if cmd[0]==100:
        create(cmd)
    elif cmd[0]==200:
        pop(cmd)
    elif cmd[0]==300:
        remove(cmd)
    elif cmd[0]==400:
        check(cmd)
    else:
        broken_belt(cmd)

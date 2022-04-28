n = int(input())
s =[list(map(int, input().split())) for _ in range(n)]
answer=999999

def combi(arr, n):
    if n==0:
        return [[]]
    result=[]
    for i in range(len(arr)):
        element = arr[i]
        for rest in combi(arr[i+1:], n-1):
            result.append([element]+rest)
    return result

start_team = combi([i for i in range(n)], n/2)
for start in start_team:
    start_num=0
    link_num=0
    for i in range(n):
        for j in range(n):
            if i in start and j in start:
                start_num+=s[i][j]
            elif i not in start and j not in start:
                link_num+=s[i][j]
    answer=min(answer, abs(start_num-link_num))
print(answer)
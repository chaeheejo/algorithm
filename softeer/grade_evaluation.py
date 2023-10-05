N = int(input())
board = [list(map(int, input().split())) for _ in range(3)]

total_board = [0]*N
rank=[]
total_rank=[]

def merge_sort(arr):
    if len(arr)<2:
        return arr
    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    merged_arr=[]
    left=right=0
    while left<len(left_arr) and right<len(right_arr):
        if left_arr[left]>right_arr[right]:
            merged_arr.append(left_arr[left])
            left+=1
        else:
            merged_arr.append(right_arr[right])
            right+=1
    merged_arr += left_arr[left:]
    merged_arr += right_arr[right:]
    return merged_arr

def count_rank(tmp_board):
    dic,idx={},0
    sorted_board = merge_sort(tmp_board)
    for s in sorted_board:
        idx+=1
        if s not in dic:
            dic[s] = idx
    result=[]
    for i in range(len(tmp_board)):
        result.append(dic[tmp_board[i]])
    print(*result)

for b in board:
    count_rank(b)
    for i in range(len(b)):
        total_board[i]+=b[i]

count_rank(total_board)
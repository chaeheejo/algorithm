from collections import defaultdict

def solution(n, results):
    answer = 0
    
    win_dict,lose_dict=defaultdict(set),defaultdict(set)
    for a,b in results:
        win_dict[a].add(b)
        lose_dict[b].add(a)
        
    for i in range(1,n+1):
        for loser in win_dict[i]:
            lose_dict[loser].update(lose_dict[i])
        for winner in lose_dict[i]:
            win_dict[winner].update(win_dict[i])
            
    for i in range(1,n+1):
        if len(win_dict[i])+len(lose_dict[i])==n-1:
            answer+=1
    
    return answer

def solution(begin, target, words):
    answer = 0
    stack = [(begin,0)]
    visited=list()
    
    while stack:
        cur,depth = stack.pop()
        
        if cur==target:
            return depth
        
        if cur not in visited:
            visited.append(cur)
            
            for word in words:
                if word not in visited:
                    cnt=0
                    for a,b in zip(cur,word):
                        if a==b:
                            cnt+=1
                    if cnt==len(word)-1 :
                        stack.append((word,depth+1))
    
    return answer

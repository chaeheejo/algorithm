def solution(n, computers):
    answer = 0
    need_visited=[]
    visited=set()
    need_visited.append(0)

    while len(visited) < n:
        node = need_visited.pop()
        visited.add(node)

        for i in range(0,n):
            if computers[node][i] == 1 and i not in visited:
                need_visited.append(i)

        if len(need_visited)==0:
            answer+=1
            for i in range(0,n):
                if i not in visited:
                    need_visited.append(i)
                    break

    if answer == 0:
        answer += 1
        
    return answer

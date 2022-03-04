def solution(record):
    answer = []
    alias = {}
    
    for i in range(0,len(record)):
        command=record[i].split(" ")
        userID = command[1]
        
        if command[0]=="Enter" or command[0]=="Change": 
            alias[userID]=command[-1]
        
    for i in range(0,len(record)):
        command=record[i].split()
        userID = command[1]
        
        if command[0]=="Enter":
            answer.append(alias[userID]+"님이 들어왔습니다.")
        elif command[0]=="Leave":
            answer.append(alias[userID]+"님이 나갔습니다.")
        
    
    return answer

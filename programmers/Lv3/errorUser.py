from itertools import permutations

def solution(user_id, banned_id):
    answer = 0

    user_permutation = list(permutations(user_id,len(banned_id)))

    answerList=[]
    for user in user_permutation:
        itemForBan=[]
        for i in range(len(banned_id)):
            if len(banned_id[i])==len(user[i]):
                check=True
                for j in range(len(banned_id[i])):
                    if banned_id[i][j]=='*':
                        continue
                    elif banned_id[i][j]!=user[i][j]:
                        check=False
                        break
                if check==True:
                    itemForBan.append(user[i])
        itemForBan.sort()
        if itemForBan not in answerList and len(itemForBan)==len(banned_id):
            answerList.append(itemForBan)

    answer=len(answerList)
    return answer

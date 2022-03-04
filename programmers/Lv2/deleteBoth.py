def solution(s):
    answer = -1

    list = [ ]

    for i in range(0,len(s)):
        if len(list) != 0 and list[-1] == s[i]:
            del (list[-1])
        else:
            list.append(s[i])

    if(len(list)==0):
        answer=1
    else:
        answer=0


    return answer

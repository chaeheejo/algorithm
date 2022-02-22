#이것이 코딩테스트다 구현 Q4-1 상하좌우

def upDownLeftRight(n, strings):
    answer = [1,1]
    for i in range(len(strings)):
        if strings[i]=='R' and answer[1]<len(strings):
            answer[1]+=1
        elif strings[i]=='U' and answer[0]>1:
            answer[0]-=1
        elif strings[i]=='D' and answer[0]<len(strings):
            answer[0]+=1

    return answer

if __name__ == '__main__':
    n=['R','R','R','U','D','D']
    answer = upDownLeftRight(5,n)
    print(answer)

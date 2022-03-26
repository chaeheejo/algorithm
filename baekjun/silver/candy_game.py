import sys

def solution():
    n = int(input())
    candyMatrix=[]

    for _ in range(n):
        line=sys.stdin.readline()
        candyMatrix.append([l for l in line[:-1]])

    def countCandy(type, index1, index2):
        if type=='c':
            result=[]
            for j in range(index1,index2+1):
                line=[]
                for i in range(n):
                    line.append(candyMatrix[i][j])
                cnt=[1]
                for i in range(1,n):
                    if line[i]==line[i-1]:
                        cnt.append(cnt[i-1]+1)
                    else:
                        cnt.append(1)
                result.append(max(cnt))
            return max(result)
        else:
            result = []
            for i in range(index1, index2 + 1):
                cnt = [1]
                for j in range(1, n):
                    if candyMatrix[i][j] == candyMatrix[i][j - 1]:
                        cnt.append(cnt[j - 1] + 1)
                    else:
                        cnt.append(1)
                result.append(max(cnt))
            return max(result)

    answer=[]
    for i in range(n):
        answer.append(countCandy('c',i,i))
        answer.append(countCandy('r',i,i))
        for j in range(n-1):
            if candyMatrix[i][j]!=candyMatrix[i][j+1]:
                candyMatrix[i][j], candyMatrix[i][j+1] = candyMatrix[i][j+1], candyMatrix[i][j]
                answer.append(countCandy('c',j,j+1))
                answer.append(countCandy('r',i,i))
                candyMatrix[i][j], candyMatrix[i][j + 1] = candyMatrix[i][j + 1], candyMatrix[i][j]
        for j in range(n - 1):
            if candyMatrix[j][i] != candyMatrix[j+1][i]:
                candyMatrix[j][i], candyMatrix[j+1][i] = candyMatrix[j+1][i], candyMatrix[j][i]
                answer.append(countCandy('r', j,j+1))
                answer.append(countCandy('c',i,i))
                candyMatrix[j][i], candyMatrix[j+1][i] = candyMatrix[j+1][i], candyMatrix[j][i]
    print(max(answer))

if __name__ == '__main__':
    answer = solution()
import copy

def solution(rows, columns, queries):
    answer = []
    array =[]
    tmpArray=[] 

    element=[]
    for i in range(columns*rows):
        if (i+1)%columns==0:
            element.append(i + 1)
            array.append(copy.deepcopy(element))
            tmpArray.append(copy.deepcopy(element))
            element=[]
        else:
            element.append(i+1)


    def minimum(edge, array):
        mini = 10000

        for i in range(edge[0], edge[2]+1):
            for j in range(edge[1], edge[3]+1):
                if i == edge[0] or i == edge[2] or j == edge[1] or j == edge[3]:
                    if mini > array[i][j]:
                        mini = array[i][j]

        return mini


    for number in range(len(queries)):
        edge = [num-1 for num in queries[number]]
        if number == len(queries)-1:
            answer.append(minimum(edge, array))

        else:
            for i in range(edge[0], edge[2]+1):
                for j in range(edge[1], edge[3]+1):
                    if i != edge[0] and i != edge[2] and j != edge[1] and j != edge[3]:
                        continue
                    if i == edge[0] and j == edge[1]: #(a,b)
                        tmpArray[i][j+1]=array[i][j]
                    elif i==edge[0] and j== edge[3]: #(a,d)
                        tmpArray[i+1][j] = array[i][j]
                    elif i == edge[2] and j == edge[1]: #(c,b)
                        tmpArray[i-1][j] = array[i][j]
                    elif i == edge[2] and j == edge[3]: #(c,d)
                        tmpArray[i][j-1] = array[i][j]
                    elif i==edge[0] : #(a,0)
                        tmpArray[i][j+1] =array[i][j]
                    elif i==edge[2] : #(c,0)
                        tmpArray[i][j-1] =array[i][j]
                    elif j==edge[1]: #(0,b)
                        tmpArray[i - 1][j] =array[i][j]
                    elif j==edge[3]: #(0,d)
                        tmpArray[i + 1][j] =array[i][j]

            array=[item[:] for item in tmpArray]
            answer.append(minimum(edge, array))


    return answer

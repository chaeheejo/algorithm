def solution(n):
    answer = []

    matrix = [[0] * i for i in range(1, n + 1)]

    def goDown(i, j, cnt, number, matrix):
        for m in range(number, number + cnt):
            i += 1
            matrix[i][j] = number
            number+=1
        return matrix

    def goRight(i, j, cnt, number, matrix):
        for m in range(number, number + cnt):
            j += 1
            matrix[i][j] = number
            number+=1
        return matrix

    def goDiagonal(i, j, cnt, number, matrix):
        for m in range(number, number + cnt):
            i -= 1
            j -= 1
            matrix[i][j] = number
            number+=1
        return matrix

    i, j, cnt, number = -1, 0, n, 1
    for m in range(1, n + 1):
        if m % 3 == 1:
            matrix = goDown(i, j, cnt, number, matrix)
            i += cnt
            number += cnt
            cnt -= 1
        elif m % 3 == 2:
            matrix = goRight(i, j, cnt, number, matrix)
            j += cnt
            number += cnt
            cnt -= 1
        else:
            matrix = goDiagonal(i, j, cnt, number, matrix)
            i -= cnt
            j -= cnt
            number += cnt
            cnt -= 1

    answer = sum(matrix, [])
    return answer

def solution(n, s, a, b, fares):
    answer = 0

    maps = [[float('inf')] * n for i in range(n)]

    for i in range(n):
        maps[i][i] = 0

    for x, y, w in fares:
        maps[x - 1][y - 1] = w
        maps[y - 1][x - 1] = w


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if maps[i][j] > maps[i][k] + maps[k][j]:
                    maps[i][j] = maps[i][k] + maps[k][j]

    answer = min([maps[i][s - 1] + maps[i][a - 1] + maps[i][b - 1] for i in range(n)])

    return answer

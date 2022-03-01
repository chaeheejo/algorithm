def solution(places):
    answer = []

    for place in places:
        loc = list()
        check = True

        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    loc.append([i, j])

        for i in range(len(loc)):
            for j in range(i + 1, len(loc)):
                if abs(loc[i][0] - loc[j][0]) + abs(loc[i][1] - loc[j][1]) == 1:
                    check = False
                    break
                elif abs(loc[i][0] - loc[j][0]) + abs(loc[i][1] - loc[j][1]) <= 2:
                    for n in range(min(loc[i][0], loc[j][0]),max(loc[i][0],loc[j][0])+1):
                        for m in range(min(loc[i][1], loc[j][1]),max(loc[i][1],loc[j][1])+1):
                            if place[n][m]=='O':
                                check=False
                                break
            if check == False:
                answer.append(0)
                break
        if check==True:
            answer.append(1)

    return answer

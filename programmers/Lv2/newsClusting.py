import math


def solution(str1, str2):
    answer = 0

    str1 = str1.upper()
    str2 = str2.upper()

    cmb1 = [str1[i:i + 2] for i in range(len(str1) - 1)]
    cmb2 = [str2[i:i + 2] for i in range(len(str2) - 1)]

    for cmb in cmb1[:]:
        if cmb.isalpha() == False:
            cmb1.remove(cmb)

    for cmb in cmb2[:]:
        if cmb.isalpha() == False:
            cmb2.remove(cmb)

    union = list(set(cmb1) | set(cmb2))
    intersection = list(set(cmb1) & set(cmb2))

    unionOverlap=[]
    intersectionOverlap=[]

    for u in union:
        for _ in range(max(cmb1.count(u), cmb2.count(u))):
            unionOverlap.append(u)

    for i in intersection:
        for _ in range(min(cmb1.count(i), cmb2.count(i))):
            intersectionOverlap.append(i)

    if len(union) != 0:
        answer = math.trunc((len(intersectionOverlap) / len(unionOverlap)) * 65536)
    elif cmb1==cmb2:
        answer = 1*65536

    return answer

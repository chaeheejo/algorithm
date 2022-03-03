from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer =[]

    for c in course:
        temp=[]

        for order in orders:
            cmb = combinations(sorted(order), c)
            temp+=cmb

        cnt=Counter(temp)

        if len(cnt)!=0 and max(cnt.values())>1:
            answer += [''.join(key) for key, value in cnt.items() if value==max(cnt.values())]

    answer.sort()
    return answer

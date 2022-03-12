from collections import defaultdict

def solution(gems):
    answer = []

    gemList = list(set(gems))
    min = len(gems)+1
    gemDict = defaultdict(lambda:0)

    start, end = 0, 0
    while end < len(gems):
        gemDict[gems[end]] += 1
        end += 1
        if len(gemDict)==len(gemList):
            while start<end:
                if gemDict[gems[start]] > 1:
                    gemDict[gems[start]] -= 1
                    start += 1
                else:
                    if end - start < min:
                        min = end - start
                        answer = [start+1, end]
                    break

    return answer

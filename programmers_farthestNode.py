from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for i in range(1, n + 1)]
    distance = [0 for i in range(n)]

    for vertex in edge:
        graph[vertex[0] - 1].append(vertex[1])
        graph[vertex[1]-1].append(vertex[0])

    needed_visit=deque([1])
    while needed_visit:
        node = needed_visit.popleft()

        for item in graph[node-1]:
            if distance[item-1]==0 and item-1!=0:
                needed_visit.append(item)
                distance[item-1] = distance[node-1] +1

    maxValue = max(distance)
    answer = distance.count(maxValue)

    return answer

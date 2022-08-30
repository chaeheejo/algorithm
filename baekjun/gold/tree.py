from collections import deque

num = int(input())
tree = list(map(str, input().split(' ')))
dieNode = input()

# graph 생성
graph = {}
for i in range(num):
    if tree[i] not in graph:  # graph에 아직 노드가 생성되지 않았다면, 새 list 생성
        graph[tree[i]] = list(str(i))
    else:  # 생성되어 있다면, item append
        graph[tree[i]].append(str(i))

visited = []
queue = deque(list(dieNode))
while queue:
    v = queue.popleft()

    if v not in visited:  # v를 방문한 적이 없으면,
        visited.append(v)

        graph[tree[int(v)]].remove(v)  # v를 자식으로 갖는 노드에서 v를 삭제

        if v in graph:  # v의 자식이 있으면, v의 자식들 추가
            queue += set(graph[v]) - set(visited)

answer = 0
for i in range(num):  # 리프 노드 개수 세기
    if str(i) not in visited:  # 방문한 적이 없음 == 삭제된 경험이 없음, 삭제되지 않은 노드들 중 자식이 없는 노드들이 세야 할 리프 노드
        if str(i) not in graph:  # graph에 저장되어 있지 않음 == 자식이 없음
            answer += 1
        elif str(i) in graph and not graph[str(i)]:  # 자식이 있으나 빈 리스트 임 == 자식이 없음
            answer += 1

print(answer)

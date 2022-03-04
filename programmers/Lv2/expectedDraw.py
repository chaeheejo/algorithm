from collections import deque

def solution(n, a, b):
    answer = 0

    if a > b:
        temp = a
        a = b
        b = temp

    queue = deque([num + 1 for num in range(n)])

    while len(queue) >= 2:
        person1 = queue.popleft()
        person2 = queue.popleft()
        winner = person1

        if person1 == a and person2 == b:
            answer+=1
            break
        if person2 == a or person2==b:
            winner = person2

        queue.append(winner)
        if person2==n:
            n=winner
            answer+=1

    return answer

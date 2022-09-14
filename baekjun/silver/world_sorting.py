N = int(input())
world = list(set([input() for _ in range(N)]))
world.sort()
world.sort(key=len)

for i in range(len(world)):
    print(world[i])
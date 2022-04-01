def solution():
    E, S, M = list(map(int, input().split()))
    e, s, m, year = 0,0,0,0

    while True:
        year+=1
        e=year%15
        s=year%28
        m=year%19

        if e==0:
            e=15
        if s==0:
            s=28
        if m==0:
            m=19

        if e == E and s == S and m == M:
            break

    print(year)

if __name__ == '__main__':
    answer = solution()
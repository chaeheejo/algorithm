T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    if n%2==0:
        print("#%d Alice" %test_case)
    else:
        print("#%d Bob" %test_case)

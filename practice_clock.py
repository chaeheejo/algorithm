#이것이 코딩 테스트다 구현Q4-2 시각

def clock(n):
    answer=0
    for i in range(n+1):
        for minute in range(60):
            for second in range(60):
                if '3' in str(i)+str(minute)+str(second):
                    answer+=1
    return answer

if __name__ == '__main__':
    answer = clock(5)
    print(answer)

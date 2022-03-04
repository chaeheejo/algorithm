def solution(n, t, m, timetable):
    answer = ''
    answerTime = 0
    timetable.sort(reverse=True)

    now = 540
    while n > 1:
        n-=1
        for _ in range(m):
            if (int(timetable[-1][:2])*60 + int(timetable[-1][-2:])) <= now:
                timetable.pop()
        now += t
    for _ in range(m - 1):
        if (int(timetable[-1][:2])*60 + int(timetable[-1][-2:])) <= now:
            timetable.pop()
    if len(timetable) != 0 and (int(timetable[-1][:2])*60 + int(timetable[-1][-2:])) <= now:
        answerTime = (int(timetable[-1][:2])*60 + int(timetable[-1][-2:])) - 1
    else:
        answerTime = now

    hour = str(answerTime // 60)
    minute = str(answerTime % 60)
    answer = hour.zfill(2) + ':' + minute.zfill(2)

    return answer

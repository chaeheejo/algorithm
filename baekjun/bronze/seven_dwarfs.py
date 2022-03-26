def solution():
    dwarfs=[]
    for _ in range(9):
        dwarfs.append(int(input()))

    for i in range(8):
        for j in range(i+1,9):
            height=0
            answer = dwarfs[:]

            for m in range(9):
                if m!=i and m!=j:
                    height+=dwarfs[m]

            if height==100:
                answer.remove(dwarfs[i])
                answer.remove(dwarfs[j])
                return answer


if __name__ == '__main__':
    answer = solution()
    answer.sort()

    for a in answer:
        print(a)